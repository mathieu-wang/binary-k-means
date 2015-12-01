import numpy as np, h5py
import time
import utils
from kmeans import kmeans
from multi_index_hashing import MihTable
import sys
from pprint import pprint

f = h5py.File('lsh_64_sift_1M.mat', 'r')
data = f.get('B')
data = np.array(data)  # For converting to numpy array
data = data[0:1000]

start_time = time.time()
# centroids = kmeans(data, 2, 64)
# print centroids

mih_table = MihTable(64, 64/8, 10)
for bit_vector in data:
    mih_table.add(bit_vector)
pprint(mih_table.hash_tables)

print("--- %s seconds ---" % (time.time() - start_time))

# array([181,  53, 218,  18, 218, 169, 186, 125], dtype=uint8), array([ 61,  27, 146,  50, 138, 193, 167, 231], dtype=uint8)