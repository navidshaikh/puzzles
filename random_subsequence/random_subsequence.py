#!/usr/bin/env python2

from random import choice


def random_subsequence(sequence, n):
    subset = []

    # loop over until len(n)
    for i in range(n):
        # pick a random index among rest of sequence elements
        # starting from current counter until last one
        picked_index = choice(range(i, len(sequence)))
        # load the random picked element
        subset.append(sequence[picked_index])
        # dead the picked element from sequence
        # give chance to seuqence[i] to be chosen again
        sequence[i] = sequence[picked_index]

    return subset


if __name__ == "__main__":
    sequence = range(10)
    n = 3
    print "Sequence {}".format(sequence)
    print "Subset {}".format(random_subsequence(sequence, 3))
