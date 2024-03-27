#!/usr/bin/python3

for char in range(97, 123):
    if char == 101 or char == 113:
        char = char + 1
    else:
        print("{:c}".format(char), end="")
