from lib.core.base_converters import Converter

if __name__ == "__main__":
    input_string = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
    expected_output_string = 'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t'

    assert Converter.convert(input_string, '16', '64') == expected_output_string
