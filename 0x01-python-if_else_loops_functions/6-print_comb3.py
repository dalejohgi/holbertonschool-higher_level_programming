#!/usr/bin/python3
counter = 1
i = 1
for counter in range(1, 9):
    while ((i % 10) != 0):
        print("{}, ".format(i).zfill(4), end='')
        i = i + 1
    i = i + counter + 1
print(89)
