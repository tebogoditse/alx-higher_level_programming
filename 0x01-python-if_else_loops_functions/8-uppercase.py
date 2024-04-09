#!/usr/bin/python3

def uppercase(str):
    new_string = ''
    for char in str:
        if ord(char) in range(97, 123):
            char = chr(ord(char) - 32)
        print(f"{char}", end="")

    print(end='\n')
