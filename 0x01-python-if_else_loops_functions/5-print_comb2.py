#!/usr/bin/python3

for i in range(0, 99):
    print("{:d}, ".format(i).zfill(4), end="")
print(i + 1)
