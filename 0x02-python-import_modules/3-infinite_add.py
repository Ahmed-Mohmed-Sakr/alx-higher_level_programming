#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    argv_c = len(argv)
    numbers_Sum = 0

    for val in range(1, argv_c):
        numbers_Sum += int(argv[val])
    print(numbers_Sum)
