#!/usr/bin/python3

for i in range(122, 96, -1):
    if not i % 2 == 0:
        c = chr(i - 32)
    else:
        c = chr(i)

    print(f"{c}", end="")
