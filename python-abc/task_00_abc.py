#!/usr/bin/python3
"""Abstract Animal Class and its Subclasses"""


from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract class Animal"""
    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):
    """Subclass Dog from Animal class"""
    def sound(self):
        """Def sound for the Dog"""
        return "Bark"


class Cat(Animal):
    """Subclass Cat from Animal class"""
    def sound(self):
        """Def sound for the Cat"""
        return "Meow"
