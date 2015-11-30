import sys
import numpy as np

def byte_array_to_long(arr):
    str = ""
    for i in arr:
        # print sys.getsizeof(i)
        b = bin(i)[2:].zfill(8)
        str+=b
    num = long(str, 2)
    # print sys.getsizeof(num)
    return num


def long_to_byte_array(num, bits):
    str = bin(num)[2:].zfill(bits)
    num_bytes = bits/8
    return np.array([int(str[i:i + num_bytes], 2) for i in range(0, len(str), num_bytes)], dtype=np.uint8)