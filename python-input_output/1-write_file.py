#!/usr/bin/python3
"""Module that defines a function to write text to a UTF-8 file."""


def write_file(filename="", text=""):
    """Writes a string to a text file and returns the num of characters wri
    tten."""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
