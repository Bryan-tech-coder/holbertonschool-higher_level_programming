#!/usr/bin/env python3
"""
This module defines mixins and a Dragon class using them.
"""


class SwimMixin:
    """Mixin that provides swimming behavior."""

    def swim(self):
        print("The creature swims!")


class FlyMixin:
    """Mixin that provides flying behavior."""

    def fly(self):
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """Dragon class that can swim and fly."""

    def roar(self):
        print("The dragon roars!")
