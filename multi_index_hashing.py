def split_chunks(bit_vector, M):
    # splits a bit vector into M chunks
    # I'll leave this as an exercise for the reader
    # eg: split_chunks(1001101110010011, 4) -> [1001, 1011, 1001, 0011]
    chunks = bit_vector
    return chunks

def generate_close_chunks(chunks, K):
    # returns a list of all possible chunks that is zero or one bit off of the input
    # I'll also leave this one for the reader
    # eg: find_close_chunks(0000) -> [0000, 1000, 0100, 0010, 0001]
    # eg: find_close_chunks(1011) -> [1011, 0011, 0111, 1001, 1010]
    close_chunks = []
    return close_chunks

class MihTable:
    def __init__(self, num_bits, num_chunks, radius):
        # called upon object creation
        self.N = num_bits
        self.M = num_chunks
        self.R = radius

        self.hash_tables = []  # a list of M hash tables

    def add(self, bit_vector):
        chunks = split_chunks(bit_vector, self.M)

        for i in xrange(self.M):
            hash_table = self.hash_tables[i]  # fetch the ith hash table
            chunk = chunks[i]  # fetch the ith chunk of the bit_vector

            if chunk not in hash_table:
                hash_table[chunk] = []

            self.bit_vector_list = hash_table[chunk]
            self.bit_vector_list.append(bit_vector)


    # K-NN search
    def lookup(self, bit_vector, K):
        chunks = split_chunks(bit_vector, self.M)

        # TODO: go in increasing search radius

        for i in xrange(self.M):
            hash_table = self.hash_tables[i]
            chunk = chunks[i]

            possible_matches = []
            close_chunks = generate_close_chunks(chunk, K)

            for close_chunk in close_chunks:
                if close_chunk in hash_table:
                    possible_matches.append(hash_table[close_chunk])

            if len(possible_matches) > 0:
                return possible_matches

        return []