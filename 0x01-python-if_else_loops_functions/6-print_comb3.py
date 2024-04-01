#!/usr/bin/python3

print("{:02d}".format(1), end="")
for number in range(2, 90):
    if str("{:02d}".format(number))[0] < str("{:02d}".format(number))[1]:
        print(f", {number:02d}", end="")

print(end='\n')
