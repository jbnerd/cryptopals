import yaml

from lib.cipher_utils.string_ops import BinaryStringOps
from lib.core.utils import StringUtils


class SingleByteEnglishXor:
    """Single byte xor cipher with English alphabet frequency scoring mechanisms"""

    def __init__(self):
        frequency_file = 'lib/cipher_utils/data/english_alphabet_frequency.yaml'
        with open(frequency_file, 'r') as fp:
            self.char_freq = yaml.safe_load(fp)

    def decode(self, bit_string):
        """
        Args:
            bit_string: (str)
        Returns:
            deciphered_string: (str)
        """
        max_sum = 0
        max_deciphered_string = ""
        for int8 in range(256):
            deciphered_string = BinaryStringOps.single_byte_xor(bit_string, int8)
            deciphered_string_int_chunks = StringUtils.binary_int_chunks(deciphered_string, 8)
            temp_sum = sum([self.char_freq.get(chr(chunk).lower(), 0) for chunk in deciphered_string_int_chunks])
            if temp_sum > max_sum:
                max_sum = temp_sum
                max_deciphered_string = ''.join([chr(chunk) for chunk in deciphered_string_int_chunks])
        return max_deciphered_string
