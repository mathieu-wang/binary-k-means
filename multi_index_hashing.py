def split_chunks(bit_vector, M):
    # splits a bit vector into M chunks
    # I'll leave this as an exercise for the reader
    # eg: split_chunks(1001101110010011, 4) -> [1001, 1011, 1001, 0011]
    chunks = bit_vector
    return chunks


def generate_close_chunks(chunk, M, radius):
    # returns a list of all possible chunks that is zero or one bit off of the input
    # I'll also leave this one for the reader
    # eg: find_close_chunks(0000) -> [0000, 1000, 0100, 0010, 0001]
    # eg: find_close_chunks(1011) -> [1011, 0011, 0111, 1001, 1010]

    chunk_rad = int(radius/M)
    close_chunks = []

    if chunk_rad == 0:
        close_chunks.append(chunk)
    elif chunk_rad == 1:
        binary = bin(chunk)[2:]
        for i in xrange(len(binary)):
            close_chunks.append(chunk ^ (1 << i))
    elif chunk_rad == 2:
        binary = bin(chunk)[2:]
        for i in xrange(len(binary)):
            for j in xrange (i+1, len(binary)):
                close_chunks.append(chunk ^ (1 << i) ^ (1 << j))
    return close_chunks

class MihTable:
    def __init__(self, num_bits, num_chunks, radius):
        # called upon object creation
        self.N = num_bits
        self.M = num_chunks
        self.R = radius

        self.hash_tables = [dict() for _ in xrange(int(self.M))]  # a list of M hash tables

    def add(self, bit_vector):
        chunks = split_chunks(bit_vector, self.M)

        for i in xrange(int(self.M)):
            hash_table = self.hash_tables[i]  # fetch the ith hash table
            chunk = chunks[i]  # fetch the ith chunk of the bit_vector

            if chunk not in hash_table:
                hash_table[chunk] = []  # make empty bit vector list

            hash_table[chunk].append(bit_vector)

    # K-NN search
    def lookup(self, bit_vector):
        chunks = split_chunks(bit_vector, self.M)

        # TODO: go in increasing search radius

        for i in xrange(int(self.M)):
            hash_table = self.hash_tables[i]
            chunk = chunks[i]

            candidates = []
            close_chunks = generate_close_chunks(chunk, self.M, self.R)

            for close_chunk in close_chunks:
                if close_chunk in hash_table:
                    candidates.append(hash_table[close_chunk])

            if len(candidates) > 0:
                print len(candidates)
                return candidates
        return []
