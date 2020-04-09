from lib.core.base_converters import Converter
from lib.core.utils import BinaryStringOps


if __name__ == "__main__":
    hex_string1 = '1c0111001f010100061a024b53535009181c'
    hex_string2 = '686974207468652062756c6c277320657965'
    expected_output_string = '746865206b696420646f6e277420706c6179'

    binary_string1 = Converter.convert(hex_string1, '16', '2')
    binary_string2 = Converter.convert(hex_string2, '16', '2')
    xor_string = BinaryStringOps.bitwise_xor(binary_string1, binary_string2)
    assert Converter.convert(xor_string, '2', '16') == expected_output_string
