from lib.cipher_utils.string_ops import HexStringOps


if __name__ == "__main__":
    hex_string1 = '1c0111001f010100061a024b53535009181c'
    hex_string2 = '686974207468652062756c6c277320657965'
    expected_output_string = '746865206b696420646f6e277420706c6179'

    assert HexStringOps.bitwise_xor(hex_string1, hex_string2) == expected_output_string
