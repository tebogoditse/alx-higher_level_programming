#!/usr/bin/python3
"""function that reads and prints a text file"""


def read_file(filename=""):
    """Reads and prints"""

    with open(filename, "r", encoding="UTF-8") as file:
        content = file.read()
        print(content, end="")
