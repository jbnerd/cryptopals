from lib.core.utils import StringUtils
from lib.core.base_converters import Converter


class BinaryStringOps:
    """Operations on binary encoded strings"""

    @staticmethod
    def bitwise_xor(binary_string1, binary_string2):
        """Performs a bitwise xor operation on binary strings

        Length of both strings after appropriate zero-padding must be equal.
        """
        chunks1 = StringUtils.binary_int_chunks(binary_string1, 8)
        chunks2 = StringUtils.binary_int_chunks(binary_string2, 8)
        if len(chunks1) != len(chunks2):
            raise ValueError('length of provided binary strings is not compatible for bitwise xor')
        xor = [i ^ j for i, j in zip(chunks1, chunks2)]
        xor_bits = [bin(i)[2:].zfill(8) for i in xor]
        return ''.join(xor_bits)

    @staticmethod
    def single_byte_xor(binary_string, int8):
        """Performs bitwise xor on binary string with int8 and a window of 8 bits"""
        byte_chunks = StringUtils.binary_int_chunks(binary_string, 8)
        xor_chunks = [bin(chunk ^ int8)[2:].zfill(8) for chunk in byte_chunks]
        return ''.join(xor_chunks)

    @staticmethod
    def hamming_distance(s1, s2):
        """Returns the Hamming distance between equal-length sequences."""
        if len(s1) != len(s2):
            raise ValueError("Undefined for sequences of unequal length.")
        return sum(el1 != el2 for el1, el2 in zip(s1, s2))


class HexStringOps:
    """Operations on hex encoded strings"""

    @staticmethod
    def bitwise_xor(hex_string1, hex_string2):
        """Performs a bitwise xor operation on binary strings

        Length of both strings after appropriate zero-padding must be equal.
        """
        if len(hex_string1) != len(hex_string2):
            raise ValueError('length of provided hex strings is not compatible for bitwise xor')
        binary_string1 = Converter.convert(hex_string1, '16', '2')
        binary_string2 = Converter.convert(hex_string2, '16', '2')
        xor_string = BinaryStringOps.bitwise_xor(binary_string1, binary_string2)
        return Converter.convert(xor_string, '2', '16')
