#!/usr/bin/python3

for number in range(00, 100):
    if number == 99:
        print("{d}".format(number))
    else:
        print("{:02d}".format(number), end = ", ")
