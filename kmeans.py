import random
import utils
import sys
from pprint import pprint
from multi_index_hashing import MihTable

MAX_ITERATIONS = 10000


def hamming_dist(num1, num2):
    dist = 0
    for i in xrange(len(num1)):
        diff = num1[i] ^ num2[i]
        cur_dist = bin(diff).count("1")
        dist += cur_dist
    return dist


# _function: _should _stop
# -------------
# _returns _true or _false if k-means is done. _k-means terminates either
# because it has run a maximum number of iterations _o_r the centroids
# stop changing.
def should_stop(old_centroids, centroids, iterations):
    if iterations > MAX_ITERATIONS:
        return True
    if old_centroids == None or centroids == None:
        return False
    for i in xrange(len(centroids)):
        pprint(old_centroids)
        pprint(centroids)
        if not (old_centroids[i] == centroids[i]).all():
            return False
    return True


def find_closest_centroid(bitvector, centroids):
    min_hamming_dist = float("inf")
    closest_centroid = None
    for centroid in centroids:
        cur_hamming_dist = hamming_dist(bitvector, centroid)
        if cur_hamming_dist < min_hamming_dist:
            min_hamming_dist = cur_hamming_dist
            closest_centroid = centroid
    return closest_centroid


def build_mih_table(mih_table, centroids):
    for centroid in centroids:
        mih_table.add(centroid)


def get_labels_mih(dataset, mih_table, radius):
    labels = []
    for bit_vector in dataset:
        for r in xrange(1, int(radius+1)):
            # candidates =
            labels.append(mih_table.lookup(bit_vector))
    return labels


# _function: _get _labels
# -------------
# _returns a label for each piece of data in the dataset.
def get_labels(dataset, centroids):
    # _for each element in the dataset, chose the closest centroid.
    # _make that centroid the element's label.
    labels = []
    for bit_vector in dataset:
        labels.append(find_closest_centroid(bit_vector, centroids))
    return labels


# _function: _get _centroids
# -------------
# _returns k random centroids, each of dimension n.
def get_centroids(dataset, labels, k, bits):
    # _each centroid is the geometric mean of the points that
    # have that centroid's label. _important: _if a centroid is empty (no points have
    # that centroid's label) you should randomly re-initialize it.
    new_centroids = []
    label_sum_dict = {}
    # sums = [0 for _ in xrange[k]]
    for idx, bit_vector in enumerate(dataset):
        number = utils.byte_array_to_long(bit_vector)
        # print labels[idx]
        label = labels[idx].tostring()
        if label not in label_sum_dict:
            label_sum_dict[label] = [0, 0]
        label_sum_dict[label][0] += number  # add to sum
        label_sum_dict[label][1] += 1  # increment counter

    # if some centroids do not have elements in their cluster, choose new ones at random
    missing_centroids = k - len(label_sum_dict)
    if missing_centroids > 0:
        new_centroids.extend(get_random_centroids(dataset, missing_centroids))

    for key, value in label_sum_dict.iteritems():
        new_centroids.append(utils.long_to_byte_array(value[0]/value[1], bits))

    return new_centroids


# Returns k centroids chosen randomly
def get_random_centroids(dataset, k):
    length = len(dataset)
    return [dataset[random.randint(0, length-1)] for _ in xrange(k)]


# _function: _k _means
# -------------
# _k-_means is an algorithm that takes in a dataset and a constant
# k and returns k centroids (which define clusters of data in the
# dataset which are similar to one another).
def kmeans(dataset, k, bits):

    # _initialize centroids randomly
    # num_features = get_num_features(dataset)
    centroids = get_random_centroids(dataset, k)

    iterations = 0
    old_centroids = None

    # _run the main k-means algorithm
    while not should_stop(old_centroids, centroids, iterations):
        print "Iteration:", iterations
        old_centroids = centroids
        iterations += 1

        # Assign labels to each datapoint based on centroids
        labels = get_labels(dataset, centroids)

        # Assign centroids based on datapoint labels
        centroids = get_centroids(dataset, labels, k, bits)

    # _we can get the labels too by calling get_labels(data_set, centroids)
    return centroids


def binary_kmeans(dataset, k, bits, radius):
    centroids = get_random_centroids(dataset, k)

    iterations = 0
    old_centroids = None

    while not should_stop(old_centroids, centroids, iterations):
        print "Iteration:", iterations
        old_centroids = centroids
        iterations += 1

        mih_table = MihTable(bits, bits/8.0, radius)

        build_mih_table(mih_table, centroids)
        # Assign labels to each datapoint based on centroids
        labels = get_labels_mih(dataset, mih_table, radius)

        # Assign centroids based on datapoint labels
        centroids = get_centroids(dataset, labels, k, bits)

    return centroids