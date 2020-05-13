from abc import abstractmethod

import yaml

from lib.cipher_utils.string_ops import BinaryStringOps
from lib.core.utils import StringUtils


class BaseCipher:
    """Skeleton class for ciphers"""

    @abstractmethod
    def encrypt(self, *args):
        raise NotImplementedError

    @abstractmethod
    def decrypt(self, *args):
        raise NotImplementedError


class SingleByteXor(BaseCipher):
    """Single byte xor cipher"""

    def encrypt(self, bit_string, int8):
        return BinaryStringOps.single_byte_xor(bit_string, int8)

    def decrypt(self, bit_string, int8):
        return BinaryStringOps.single_byte_xor(bit_string, int8)


class SingleByteXorEnglish(BaseCipher):
    """Single byte xor cipher with english alphabet frequency as a scoring mechanism"""

    def __init__(self):
        frequency_file = 'lib/cipher_utils/data/english_alphabet_frequency.yaml'
        with open(frequency_file, 'r') as fp:
            self.char_freq = yaml.safe_load(fp)

    def encrypt(self, bit_string, int8):
        return BinaryStringOps.single_byte_xor(bit_string, int8)

    def decrypt(self, bit_string):
        best_score, best_deciphered_string, best_key = 0, "", -1
        for int8 in range(256):
            xored_bit_string = BinaryStringOps.single_byte_xor(bit_string, int8)
            xored_bit_string_chunks = StringUtils.binary_int_chunks(xored_bit_string, 8)
            score = sum([self.char_freq.get(chr(chunk).lower(), 0) for chunk in xored_bit_string_chunks])
            if score > best_score:
                best_score = score
                best_deciphered_string = ''.join([chr(chunk) for chunk in xored_bit_string_chunks])
                best_key = chr(int8)
        return best_deciphered_string, best_score, best_key


class RepeatingKeyXor(BaseCipher):
    """Single byte xor cipher with repeating keys

        The keys are repeated by sampling a character from a string in a round-robin fashion
    """

    def encrypt(self, data_string, key_string):
        data_bit_string = StringUtils.string_to_bit_string(data_string)
        key_bit_string = StringUtils.string_to_bit_string(key_string)

        repeat_mul = int(len(data_bit_string) / len(key_bit_string)) + 1
        key_bit_string = key_bit_string * repeat_mul
        key_bit_string = key_bit_string[:len(data_bit_string)]

        resultant_string = BinaryStringOps.bitwise_xor(data_bit_string, key_bit_string)
        return resultant_string

    def decrypt(self, data):
        candidate_key_lengths = self._choose_candidate_key_lengths(data)
        best_key, best_score = "", 0
        for candidate_key_len in candidate_key_lengths:
            key, score = self._find_key(data, candidate_key_len)
            if score > best_score:
                best_key = key
                best_score = score
        return best_key

    def _choose_candidate_key_lengths(self, data, max_key_len=41, num_candidates=3):
        candidates = []
        for i in range(2, max_key_len):
            chunks = StringUtils.make_chunks(data, i * 8)
            mean_score = self._mean_xor_score(chunks)
            candidates.append((i, mean_score))
        candidates = sorted(candidates, key=lambda x: x[1])
        candidates = [candidate[0] for candidate in candidates]
        return candidates[:num_candidates]

    def _mean_xor_score(self, chunks):
        scores = []
        while True:
            try:
                scores.append(self._normalized_xor_score(chunks[0], chunks[1]))
                del chunks[0]
                del chunks[1]
            except:
                break
        return sum(scores) / len(scores)

    @staticmethod
    def _normalized_xor_score(chunk1, chunk2):
        score = BinaryStringOps.hamming_distance(chunk1, chunk2)
        return float(score) / len(chunk1)

    def _find_key(self, data, key_len):
        transposed_blocks = self._transposed_blocks(data, key_len)
        key, score = "", 0
        single_byte_xor_cipher = SingleByteXorEnglish()
        for block in transposed_blocks:
            _, block_score, block_key = single_byte_xor_cipher.decrypt(block)
            key += block_key
            score += block_score
        return key, score

    @staticmethod
    def _transposed_blocks(data, key_len):
        chunks = StringUtils.make_chunks(data, 8)
        blocks = [chunks[i: i + key_len] for i in range(0, len(chunks), key_len)]
        transposed_blocks = []
        for i in range(key_len):
            transposed_block = []
            for block in blocks:
                if i < len(block):
                    transposed_block.append(block[i])
            transposed_blocks.append(transposed_block)
        transposed_blocks = [''.join(block) for block in transposed_blocks]
        return transposed_blocks
