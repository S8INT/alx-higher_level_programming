#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for colum in matrix:
            print("{:}".format(colum), end= " " if colum != row[-1] else "")
        print()
