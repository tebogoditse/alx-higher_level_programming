#!/usr/bin/python3

def uppercase(str):
    new_string = ''
    for char in str:
        if ord(char) in range(97, 123):
            new_string = new_string + chr(ord(char) - 32)
        else:
            new_string = new_string + chr(ord(char))

    print(f"{new_string}")
