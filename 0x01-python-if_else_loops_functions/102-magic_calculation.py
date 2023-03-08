#!/usr/bin/python3
# this program works exactly like the python bytecode
def magic_calculation(a, b, c):
    if a < b:
        return c
    elif c > b:
        return a + b

    return a * b - c
