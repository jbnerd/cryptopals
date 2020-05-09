import yaml
from abc import abstractmethod

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
        best_score, best_deciphered_string = 0, ""
        for int8 in range(256):
            xored_bit_string = BinaryStringOps.single_byte_xor(bit_string, int8)
            xored_bit_string_chunks = StringUtils.binary_int_chunks(xored_bit_string, 8)
            score = sum([self.char_freq.get(chr(chunk).lower(), 0) for chunk in xored_bit_string_chunks])
            if score > best_score:
                best_score = score
                best_deciphered_string = ''.join([chr(chunk) for chunk in xored_bit_string_chunks])
        return best_deciphered_string, best_score
