class StringUtils:
    """Operations on binary encoded strings"""

    @staticmethod
    def make_chunks(string, chunk_len):
        if len(string) % chunk_len == 0:
            required_len = len(string)
        else:
            required_len = len(string) + chunk_len - (len(string) % chunk_len)
        string = string.zfill(required_len)
        return [string[i: i + chunk_len] for i in range(0, len(string), chunk_len)]

    @classmethod
    def binary_int_chunks(cls, binary_string, chunk_len):
        chunks = cls.make_chunks(binary_string, chunk_len)
        return [int(chunk, 2) for chunk in chunks]
