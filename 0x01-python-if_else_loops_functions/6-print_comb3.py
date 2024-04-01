#!/usr/bin/python3

first_digit = 0
print("{:02d}".format(first_digit), end="")
for number in range(1, 90):
    number = "{:02d}".format(number)
    if str(number)[0] < str(number)[1]:
        print(f", {number}", end="")

print(end='\n')
