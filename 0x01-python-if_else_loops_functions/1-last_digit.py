#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)
remainder = 0

if number < 0:
    remainder = number % -10
else:
    remainder = number % 10

message = f"Last digit of {number} is {remainder}"

if remainder > 5:
    print(f"{message} and is greater than 5")
elif remainder == 0:
    print(f"{message} and is 0")
else:
    print(f"{message} and is less than 6 and not 0")
