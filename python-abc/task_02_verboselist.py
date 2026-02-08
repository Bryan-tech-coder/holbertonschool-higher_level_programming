#!/usr/bin/env python3
"""
This module defines a VerboseList class that extends the built-in list
and prints notifications on modifications.
"""


class VerboseList(list):
    """
    A list that prints messages when modified.
    """

    def append(self, item):
        """
        Adds an item to the list and prints a notification.
        """
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, iterable):
        """
        Extends the list and prints a notification with number of items added.
        """
        count = len(iterable)
        super().extend(iterable)
        print(f"Extended the list with [{count}] items.")

    def remove(self, item):
        """
        Removes an item from the list and prints a notification.
        """
        print(f"Removed [{item}] from the list.")
        super().remove(item)

    def pop(self, index=-1):
        """
        Pops an item from the list and prints a notification.
        """
        item = self[index]
        print(f"Popped [{item}] from the list.")
        return super().pop(index)
