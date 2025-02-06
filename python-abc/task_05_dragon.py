#!/usr/bin/python3
"""The Mystical Dragon - Mastering Mixins"""


class SwimMixin:
    """mixin class and method"""
    def swim(self):
        """print method for swim"""
        print("The creature swims!")


class FlyMixin:
    """mixin class and method"""
    def fly(self):
        """print method fr fly"""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """class call the mixin class"""
    def roar(self):
        """new print method called"""
        print("The dragon roars!")
