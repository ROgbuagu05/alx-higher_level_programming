#!/usr/bin/python3
for i in range(10):
    for j in range(10):
        if i < j:
            if i == 0 and j == 1:
                print("01", end="")
            else:
                print("{:d}{:d}".format(i, j), end="")
            if i != 8 or j != 9:
                print(", ", end="")
            else:
                print("\n", end="")
