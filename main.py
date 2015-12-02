import numpy as np, h5py
import time
import utils
from kmeans import kmeans
from kmeans import binary_kmeans
from kmeans import get_labels
from kmeans import get_labels_mih
from kmeans import get_random_centroids
from multi_index_hashing import MihTable
import sys
from pprint import pprint

f = h5py.File('lsh_64_sift_1M.mat', 'r')
data = f.get('B')
data = np.array(data)  # For converting to numpy array
data = data[0:10000]

for i in xrange(100, 1100, 100):
    # print i
    start_time = time.time()
    # centroids = kmeans(data, 2, 64)
    # print centroids

    mih_table = MihTable(64, 64/8, 10)
    for bit_vector in data:
        mih_table.add(bit_vector)
    print "Done building MIH table"
    print("--- %s seconds ---" % (time.time() - start_time))

    centroids = get_random_centroids(data, i)
    # get_labels(data, centroids)
    labels = get_labels_mih(data, mih_table, 16)

    print("--- %s seconds ---" % (time.time() - start_time))

# print(labels)

# array([181,  53, 218,  18, 218, 169, 186, 125], dtype=uint8), array([ 61,  27, 146,  50, 138, 193, 167, 231], dtype=uint8)