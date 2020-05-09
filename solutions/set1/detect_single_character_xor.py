from lib.cipher_utils.ciphers import SingleByteXorEnglish
from lib.core.base_converters import Converter


def read_file():
    file_name = 'solutions/set1/data/detect_single_character_xor.in'
    with open(file_name, 'r') as infile:
        lines = infile.read().split('\n')[:-1]
    return lines


def main():
    decipherer = SingleByteXorEnglish()
    lines = read_file()
    max_score, best_deciphered_string = 0, None
    for line in lines:
        binary_string = Converter.convert(line, '16', '2')
        deciphered_string, score = decipherer.decrypt(binary_string)
        if score > max_score:
            max_score = score
            best_deciphered_string = deciphered_string
    print(best_deciphered_string)


if __name__ == "__main__":
    main()
