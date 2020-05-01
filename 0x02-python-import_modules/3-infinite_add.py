#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    i = 1
    result = 0
    for i in range(1, len(sys.argv)):
        number = int(sys.argv[i])
        result += number
    print(result)
