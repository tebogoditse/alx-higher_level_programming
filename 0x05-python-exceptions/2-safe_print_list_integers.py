#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    count = 0
    i = 0
    for i in range(0, x):
        try:
            print("{:d}".format(my_list[i]), end="")
        except (ValueError, TypeError):
            continue
        else:
            count += 1
    print(end="\n")
    return count
