#!/usr/bin/python3
"""CountedIterator - Keeping Track of Iteration"""


class CountedIterator:
    """abstract class countediterator"""
    def __init__(self, some_iterable):
        """initialize two attributes"""
        self.iterator = iter(some_iterable)
        self.count = 0

    def __iter__(self):
        """iter function"""
        return self

    def __next__(self):
        """increment the counter each time the __next__ method is called"""
        item = next(self.iterator)
        if not item:
            raise StopIteration
        self.count += 1
        return item

    def get_count(self):
        """to retrieve and print the number of items that have been fetched"""
        return self.count
