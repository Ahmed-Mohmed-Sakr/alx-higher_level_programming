#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):

    row_len = 0
    for row in matrix:
        row_len = len(row)
        for item in row:
            if (row_len > 1):
                print("{:d}".format(item), end=" ")
            else:
                print("{:d}".format(item), end="")
            row_len -= 1
        print()
