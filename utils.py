import sys


def byte_array_to_long(arr):
    str = ""
    for i in arr:
        # print sys.getsizeof(i)
        b = bin(i)[2:].zfill(8)
        str+=b
    num = long(str, 2)
    # print sys.getsizeof(num)
    return num