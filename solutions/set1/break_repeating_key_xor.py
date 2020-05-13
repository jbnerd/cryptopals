from lib.cipher_utils.ciphers import RepeatingKeyXor
from lib.cipher_utils.string_ops import BinaryStringOps
from lib.core.base_converters import Converter
from lib.core.utils import StringUtils


def test_hamming_distance():
    str1, str2 = 'this is a test', 'wokka wokka!!!'
    str1, str2 = StringUtils.string_to_bit_string(str1), StringUtils.string_to_bit_string(str2)
    assert BinaryStringOps.hamming_distance(str1, str2) == 37


def read_data():
    with open('solutions/set1/data/break_repeating_key_xor.in', 'r') as infile:
        data = infile.read().strip().split('\n')
    return ''.join(data)


def main():
    data = read_data()
    bit_string = Converter.convert(data, '64', '2')
    cipher = RepeatingKeyXor()
    print(cipher.decrypt(bit_string))


if __name__ == "__main__":
    test_hamming_distance()
    main()
