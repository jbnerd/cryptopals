class BinaryStringOps:
    """Operations on binary encoded strings"""

    @staticmethod
    def int_chunks(binary_string, chunk_len):
        if len(binary_string) % chunk_len == 0:
            required_len = len(binary_string)
        else:
            required_len = len(binary_string) + chunk_len - (len(binary_string) % chunk_len)
        binary_string = binary_string.zfill(required_len)
        chunks = [binary_string[i: i + chunk_len] for i in range(0, len(binary_string), chunk_len)]
        return [int(chunk, 2) for chunk in chunks]

    @classmethod
    def bitwise_xor(cls, binary_string1, binary_string2):
        """Performs a bitwise xor operation on binary strings

        Length of both strings after appropriate zero-padding must be equal.
        """
        chunks1 = cls.int_chunks(binary_string1, 8)
        chunks2 = cls.int_chunks(binary_string2, 8)
        if len(chunks1) != len(chunks2):
            raise ValueError('length of provided binary strings is not compatible for bitwise xor')
        xor = [i ^ j for i, j in zip(chunks1, chunks2)]
        xor_bits = [bin(i)[2:].zfill(8) for i in xor]
        return ''.join(xor_bits)
