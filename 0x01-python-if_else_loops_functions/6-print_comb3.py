#!/usr/bin/python3
for digit in range(0, 9):
    for digit1 in range(digit + 1, 10):
        if digit == 8:
            print("{:d}{:d}".format(digit, digit1))
            break
        print("{:d}{:d}".format(digit, digit1), end=", ")
