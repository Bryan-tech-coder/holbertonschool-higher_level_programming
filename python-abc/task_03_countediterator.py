#!/usr/bin/env python3
"""
This module defines a CountedIterator class that counts
how many items have been iterated.
"""


class CountedIterator:
    """
    Iterator that counts the number of items fetched.
    """

    def __init__(self, iterable):
        """
        Initializes the iterator and counter.
        """
        self.iterator = iter(iterable)
        self.count = 0

    def __next__(self):
        """
        Returns the next item and increments the counter.
        """
        item = next(self.iterator)  # may raise StopIteration
        self.count += 1
        return item

    def get_count(self):
        """
        Returns the number of items iterated so far.
        """
        return self.count
