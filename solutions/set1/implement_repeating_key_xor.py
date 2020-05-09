from lib.cipher_utils.ciphers import RepeatingKeyXor
from lib.core.base_converters import Converter


if __name__ == "__main__":
    data_string = "Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"
    key_string = "ICE"
    expected_result = open('solutions/set1/data/implement_repeating_key_xor.in').read().strip()
    decipherer = RepeatingKeyXor()
    result = decipherer.encrypt(data_string, key_string)
    result = Converter.convert(result, '2', '16')
    assert result == expected_result
