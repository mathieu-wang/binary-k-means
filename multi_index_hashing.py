import sys
import numpy as np, h5py
import kmeans

f = h5py.File('lsh_64_sift_1M.mat', 'r')
data = f.get('B')
data = np.array(data) # For converting to numpy array
# print data[0]
# for i in data[0]:
#     b = bin(i)[2:].zfill(8)
#     print sys.getsizeof(b)

print kmeans.get_random_centroids(data, 10)