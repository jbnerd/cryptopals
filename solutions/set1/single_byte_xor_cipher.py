from lib.cipher_utils.ciphers import SingleByteXorEnglish
from lib.core.base_converters import Converter

if __name__ == "__main__":
    hex_string = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
    binary_string = Converter.convert(hex_string, '16', '2')
    decipherer = SingleByteXorEnglish()
    print(decipherer.decrypt(binary_string)[0])
