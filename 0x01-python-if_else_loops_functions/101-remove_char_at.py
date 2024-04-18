#!/usr/bin/python3

def remove_char_at(str, n):

    new_str = ""
    for i in range(0, len(str)):
        if not i == n:
            new_str += str[i]
        else:
            i += 1
    return new_str
