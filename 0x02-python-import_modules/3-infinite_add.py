#!/usr/bin/python3
# Prints the result of the addition of all arguments
from sys import argv

if __name__ == "__main__":
    total = 0
    i = 0
    for arg in argv:
        if not i == 0:
            total += int(arg)
        i += 1

    print("{:d}".format(total))
