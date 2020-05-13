import string

from lib.core.utils import StringUtils


class ConversionDataGenerator:
    """Generates data for base conversion logic"""

    @classmethod
    def base16_mappings(cls):
        num_str = ''.join([str(i) for i in range(10)])
        alpha_str = string.ascii_lowercase[:6]
        int_to_base16 = num_str + alpha_str
        base16_to_int = {letter: i for i, letter in enumerate(int_to_base16)}
        return base16_to_int, int_to_base16

    @classmethod
    def base64_mappings(cls):
        upper_case_alpha_str = string.ascii_uppercase
        lower_case_alpha_str = string.ascii_lowercase
        num_str = ''.join([str(i) for i in range(10)])
        extras_str = '+/'
        int_to_base64 = upper_case_alpha_str + lower_case_alpha_str + num_str + extras_str
        base64_to_int = {letter: i for i, letter in enumerate(int_to_base64)}
        return base64_to_int, int_to_base64


class Converter:
    """Conversion logic for all supported bases"""

    _base16_to_int, _int_to_base16 = ConversionDataGenerator.base16_mappings()
    _base64_to_int, _int_to_base64 = ConversionDataGenerator.base64_mappings()
    _base2_names = ['binary', 'bin', '2', 'base2']
    _base16_names = ['hexadecimal', 'hex', '16', 'base16']
    _base64_names = ['64', 'base64']
    _supported_base_names = _base2_names + _base16_names + _base64_names

    @classmethod
    def convert(cls, input_str, from_base, to_base):
        cls._check_for_supported_base(from_base, to_base)
        try:
            if from_base in cls._base16_names:
                intermediate_result = cls._base16_to_binary_string(input_str)
            elif from_base in cls._base64_names:
                intermediate_result = cls._base64_to_binary_string(input_str)
            else:
                intermediate_result = input_str

            if to_base in cls._base16_names:
                return cls._binary_string_to_base16(intermediate_result)
            elif to_base in cls._base64_names:
                return cls._binary_string_to_base64(intermediate_result)
            else:
                return intermediate_result
        except:
            raise ValueError('input_str has characters not supported by from_base')

    @classmethod
    def _check_for_supported_base(cls, from_base, to_base):
        if from_base not in cls._supported_base_names:
            raise ValueError('from_base parameter value not supported. Try one of the following:\n'
                             + str(cls._supported_base_names))
        if to_base not in cls._supported_base_names:
            raise ValueError('to_base parameter value not supported. Try one of the following:\n'
                             + str(cls._supported_base_names))

    @staticmethod
    def _base16_to_binary_string(base16_str):
        """Converts a base16 string into binary string

        Args:
            base16_str: (str)

        Returns:
            binary encoding of input string: (str)
        """
        binary_string = bin(int(base16_str, 16))[2:]
        return StringUtils.lfill_required_len(binary_string, 8)

    @classmethod
    def _binary_string_to_base16(cls, binary_string):
        """Converts a binary string into base16 string

        Args:
            binary_string: (str)

        Returns:
            base16 encoding of input string: (str)
        """
        chunks = StringUtils.binary_int_chunks(binary_string, chunk_len=4, pad='left')
        return ''.join([cls._int_to_base16[chunk] for chunk in chunks])

    @staticmethod
    def _count_base64_padding_chars(base64_str):
        return len(base64_str) - len(base64_str.rstrip('='))

    @classmethod
    def _base64_to_binary_string(cls, base64_str):
        """Converts a base64 string into binary string

        Args:
            base64_str: (str)

        Returns:
            binary encoding of input string: (str)
        """
        num_padding_chars = cls._count_base64_padding_chars(base64_str)
        base64_str = base64_str.rstrip('=')
        bit_string = ''.join([bin(cls._base64_to_int[letter])[2:].zfill(6) for letter in base64_str])
        if num_padding_chars == 0:
            pass
        elif num_padding_chars == 1:
            bit_string = bit_string[:-2]
        elif num_padding_chars == 2:
            bit_string = bit_string[:-4]
        else:
            raise ValueError('Encountered absurd number of padding characters')
        return bit_string.lstrip('0')

    @classmethod
    def _binary_string_to_base64(cls, binary_string):
        """Converts a binary string into base64 string

        Args:
            binary_string: (str)

        Returns:
            base64 encoding of input string: (str)
        """
        chunks = StringUtils.binary_int_chunks(binary_string, 6, pad='right')
        base_64_str = ''.join([cls._int_to_base64[chunk] for chunk in chunks])
        return StringUtils.rfill_required_len(base_64_str, 4, custom_char='=')
