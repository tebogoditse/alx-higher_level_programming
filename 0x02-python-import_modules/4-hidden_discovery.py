#!/usr/bin/python3
# Prints all the names defined by the compiled module [hidden_4.pyc]
import hidden_4

if __name__ == "__main__":
    name = dir(hidden_4)
    for i in name:
        if not i[0:2] == "__":
            print("{:s}".format(i))
