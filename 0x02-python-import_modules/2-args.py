#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    i = 1
    if (len(sys.argv) == 1):
        print("0 arguments.")
    elif (len(sys.argv) == 2):
        print("{:d} argument:".format(i))
    else:
        print("{:d} arguments:".format(len(sys.argv) - 1))
    if (len(sys.argv) != 1):
        for i in range(1, len(sys.argv)):
            print("{}: {}".format(i, sys.argv[i]))
