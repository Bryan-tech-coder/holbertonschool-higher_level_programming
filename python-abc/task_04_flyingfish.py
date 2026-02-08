#!/usr/bin/env python3
"""
This module defines Fish, Bird, and FlyingFish classes
to demonstrate multiple inheritance and MRO.
"""


class Fish:
    """Represents a fish."""

    def swim(self):
        print("The fish is swimming")

    def habitat(self):
        print("The fish lives in water")


class Bird:
    """Represents a bird."""

    def fly(self):
        print("The bird is flying")

    def habitat(self):
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """Represents a flying fish using multiple inheritance."""

    def fly(self):
        print("The flying fish is soaring!")

    def swim(self):
        print("The flying fish is swimming!")

    def habitat(self):
        print("The flying fish lives both in water and the sky!")
