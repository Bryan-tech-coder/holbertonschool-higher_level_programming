#!/usr/bin/env python3
"""Module that defines a CustomObject class with pickle serialization."""

import pickle


class CustomObject:
    """Custom object that can be serialized/deserialized with pickle."""

    def __init__(self, name, age, is_student):
        """Initialize the CustomObject."""
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Display the object's attributes."""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """
        Serialize the current instance to a file using pickle.
        Returns None if an error occurs.
        """
        try:
            with open(filename, "wb") as f:
                pickle.dump(self, f)
        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename):
        """
        Deserialize an instance from a pickle file.
        Returns the object, or None if an error occurs.
        """
        try:
            with open(filename, "rb") as f:
                obj = pickle.load(f)
                return obj
        except Exception:
            return None
