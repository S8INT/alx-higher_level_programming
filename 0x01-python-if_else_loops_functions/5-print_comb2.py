#!/usr/bin/python3
for n in range(100):
    if n == 99:
        print(n)
    else:
        print("{}".format('0' + str(n) if n < 10 else n), end=", ")
