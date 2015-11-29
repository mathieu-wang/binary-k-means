import sys
import numpy as np, h5py
import kmeans

f = h5py.File('lsh_64_sift_1M.mat', 'r')
data = f.get('B')
data = np.array(data) # For converting to numpy array
# print data[0]
# for i in data[0]:
#     b = bin(i)[2:].zfill(8)
# #     print sys.getsizeof(b)
#     print b,
#
# print ""
# for i in data[1]:
#     b = bin(i)[2:].zfill(8)
#     print b,

# print kmeans.get_random_centroids(data, 10)
# print kmeans.hamming_dist(data[0], data[1])
# print kmeans.hamming_dist([7, 6], [4, 5])
print kmeans.find_closest_centroid(data[0], kmeans.get_random_centroids(data, 100))
# array([181,  53, 218,  18, 218, 169, 186, 125], dtype=uint8), array([ 61,  27, 146,  50, 138, 193, 167, 231], dtype=uint8)