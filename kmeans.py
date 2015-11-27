import random


MAX_ITERATIONS = 100

# _function: _should _stop
# -------------
# _returns _true or _false if k-means is done. _k-means terminates either
# because it has run a maximum number of iterations _o_r the centroids
# stop changing.
def should_stop(old_centroids, centroids, iterations):
    if iterations > MAX_ITERATIONS: return True
    return old_centroids == centroids

# _function: _get _labels
# -------------
# _returns a label for each piece of data in the dataset.
def get_labels(data_set, centroids):
    # _for each element in the dataset, chose the closest centroid.
    # _make that centroid the element's label.
    pass

# _function: _get _centroids
# -------------
# _returns k random centroids, each of dimension n.
def get_centroids(data_set, labels, k):
    # _each centroid is the geometric mean of the points that
    # have that centroid's label. _important: _if a centroid is empty (no points have
    # that centroid's label) you should randomly re-initialize it.
    pass


def get_random_centroids(dataset, k):
    length = len(dataset)
    return [random.randint(0, length) for _ in xrange(k)]


def get_num_features(dataset):
    pass

# _function: _k _means
# -------------
# _k-_means is an algorithm that takes in a dataset and a constant
# k and returns k centroids (which define clusters of data in the
# dataset which are similar to one another).
def kmeans(dataset, k):

    # _initialize centroids randomly
    num_features = get_num_features(dataset)
    centroids = get_random_centroids(num_features, k)

    # _initialize book keeping vars.
    iterations = 0
    old_centroids = None

    # _run the main k-means algorithm
    while not should_stop(old_centroids, centroids, iterations):
        # _save old centroids for convergence test. _book keeping.
        old_centroids = centroids
        iterations += 1

        # _assign labels to each datapoint based on centroids
        labels = get_labels(dataset, centroids)

        # _assign centroids based on datapoint labels
        centroids = get_centroids(dataset, labels, k)

    # _we can get the labels too by calling get_labels(data_set, centroids)
    return centroids
