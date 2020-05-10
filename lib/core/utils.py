class StringUtils:
    """Operations on binary encoded strings"""

    @classmethod
    def binary_int_chunks(cls, binary_string, chunk_len, pad='left'):
        chunks = cls.make_chunks(binary_string, chunk_len, pad)
        return [int(chunk, 2) for chunk in chunks]

    @classmethod
    def make_chunks(cls, string, chunk_len, pad='left'):
        if pad not in ['left', 'right']:
            raise ValueError('padding can either be "left" or "right"')

        if pad == 'left':
            string = cls.lfill_required_len(string, chunk_len)
        else:
            string = cls.rfill_required_len(string, chunk_len)
        return [string[i: i + chunk_len] for i in range(0, len(string), chunk_len)]

    @classmethod
    def lfill_required_len(cls, string, chunk_len, custom_char='0'):
        required_len = cls._required_divisible_len(len(string), chunk_len)
        num_chars = required_len - len(string)
        return cls.lfill(string, num_chars, custom_char)

    @staticmethod
    def _required_divisible_len(curr_len, divisor):
        if curr_len % divisor == 0:
            required_len = curr_len
        else:
            required_len = curr_len + divisor - (curr_len % divisor)
        return required_len

    @staticmethod
    def lfill(string, num_char, custom_char='0'):
        return custom_char * num_char + string

    @classmethod
    def rfill_required_len(cls, string, chunk_len, custom_char='0'):
        required_len = cls._required_divisible_len(len(string), chunk_len)
        num_chars = required_len - len(string)
        return cls.rfill(string, num_chars, custom_char)

    @staticmethod
    def rfill(string, num_chars, custom_char='0'):
        return string + custom_char * num_chars

    @staticmethod
    def string_to_bit_string(string):
        ascii_list = [ord(char) for char in string]
        bit_string = ''.join([bin(char)[2:].zfill(8) for char in ascii_list])
        return bit_string
