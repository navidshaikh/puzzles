#!/usr/bin/env python2

import sys

class Node(object):
    def __init__(self, value):
        self.mid = value
        self.left = None
        self.right = None


class IntervalSearch(object):
    """
    Interval Search class aggregating utilities methods
    Loads given interval (unbalanced) binary tree
    and performs search by traversing through tree
    """
    def __init__(self):
        self.root = None
    def mid_point(self, interval):
        """
        Finds mid point given a range of interval
        """
        init = interval[0]
        last = interval[1]
        interval_range =range(int(init), int(init))
        if not interval_range:
            # cases for [-0.9, -0.1]
            return (init + last)/2

        mid_index = len(interval_range)/2
        return interval_range[mid_index]

    def _add_node(self, parent, child):
        """
        Sub add_node method to handle adding nodes
        based on the interval values
        """
        if parent.left:
            if parent.left.mid >= child.left.mid:
                if parent.left.left is None:
                    parent.left.left = child
                else:
                    self._add_node(parent.left, child)
        if parent.right:
            if parent.right.mid <= child.right.mid:
                if parent.right.right is None:
                    parent.right.right = child
                else:
                    self._add_node(parent.right, child)

    def add_node(self, new_node):
        """
        Add given node to tree data structure
        """
        # case for first/root node
        if self.root is None:
            self.root = new_node
        else:
            self._add_node(self.root, new_node)

    def index_interval(self, interval):
        """
        each init, mid, last of an interval
        is an object of Node class
        """
        mp = self.mid_point(interval)
        new_node = Node(mp)
        new_node.left = Node(interval[0])
        new_node.right = Node(interval[-1])
        self.add_node(new_node)

    def load_intervals(self, intervals):
        """
        Iterates over intervals and index each in tree
        """
        for interval in intervals:
            self.index_interval(interval)

    def _search(self, n, node):
        """
        sub _search method to perform recursive searches
        """
        # found at mid
        if node.mid == n:
            return True
        # reached leaf node
        if not node.left and not node.right:
            return False
        # path to right wing of tree
        if not node.left:
            if node.right:
                return self._search(n, node.right)
        # path to left wing of tree
        if not node.right:
            if node.left:
                return self._search(n, node.left)

        # path where left and right wing exists
        if node.left and node.right:
            # check if point is available in interval
            if node.left.mid <= n <= node.right.mid:
                return True
            # decide whether traverse to right?
            if n > node.right.mid:
                return self._search(n, node.right)
            else:
                # decide whether traverse to left?
                if n < node.left.mid:
                    return self._search(n, node.left)
        else:
            # case where point not found in tree
            return False

    def search(self, point):
        """
        Search utitlity to find an point
        in loaded intervals
        """
        if self.root is None:
            return False
        else:
            return self._search(point, self.root)


if __name__ == "__main__":
    # non overlapping
    t1 = [[-100, -50], [-20, 0], [1, 33], [44,46], [50, 55]]
    # overlapping
    t2 = [[-100, -88], [-10,10], [-1.3, 2.3], [-20, 0], [1, 55]]

    print "=============Sample test cases========="
    print "Non-overlapping: {}".format(t1)
    print "Overlapping:     {}".format(t2)

    if len(sys.argv) < 2 :
        print "Please provide point to search."
        print "Example: python interval_search.py -0.5"
        sys.exit(1)
    else:
        point = float(sys.argv[1].strip())

    for t in [t1, t2]:
        print "Finding {} in intervals: {}".format(point, t)
        its_obj = IntervalSearch()
        its_obj.load_intervals(t)
        print its_obj.search(point)
