#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    argv_c = len(argv)

    if argv_c == 1:
        print("{} argument.".format(argv_c - 1))
    else:
        print("{} argument:".format(argv_c - 1))
        for val in range(1, argv_c):
            print("{}: {}".format(val, argv[val]))
