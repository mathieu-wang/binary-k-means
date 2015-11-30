import numpy as np, h5py
import time
import utils
from kmeans import get_centroids, get_labels, get_random_centroids
import sys

f = h5py.File('lsh_64_sift_1M.mat', 'r')
data = f.get('B')
data = np.array(data)  # For converting to numpy array
data = data[0:10000]
print sys.getsizeof(data[0][0])

# print sys.getsizeof(data[0])
# print data[0].nbytes
# print len(data)

# print utils.byte_array_to_long(data[0])

# print kmeans.get_random_centroids(data, 10)
# print kmeans.hamming_dist(data[0], data[1])
# print kmeans.hamming_dist([7, 6], [4, 5])

# print data[0].tostring()

start_time = time.time()
# for point in data:
#     kmeans.find_closest_centroid(point, kmeans.get_random_centroids(data, 1))
# print bin(data[0])
initial_centroids = get_random_centroids(data, 10)
print initial_centroids
labels = get_labels(data, initial_centroids)
print len(labels)
centroids = get_centroids(data, labels, 10)
print centroids
for centroid in centroids:
    # print sys.getsizeof(centroid)
    print utils.long_to_byte_array(centroid, 64).nbytes
print("--- %s seconds ---" % (time.time() - start_time))

# array([181,  53, 218,  18, 218, 169, 186, 125], dtype=uint8), array([ 61,  27, 146,  50, 138, 193, 167, 231], dtype=uint8)