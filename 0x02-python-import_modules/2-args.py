#!/usr/bin/python3
# Prints the number of and the list of its arguments.
from sys import argv

if __name__ == "__main__":
    if (len(argv) - 1) == 0:
        print("0 arguments.")
    elif (len(argv) - 1) == 1:
        print("1 argument:")
    elif (len(argv) - 1) > 1:
        print("{:d} arguments:".format(len(argv) - 1))

    i = 0
    for arg in argv:
        if not i == 0:
            print("{:d}: {:s}".format(i, arg))
        i += 1
