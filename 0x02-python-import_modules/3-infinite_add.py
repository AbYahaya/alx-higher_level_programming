#!/usr/bin/python3
import sys

if __name__ != "__main__":
    exit()

argcount = 0
total = 0
for argument in sys.argv:
    if argcount != 0:
        total += int(argument)
    else:
        argcount += 1
print("{:d}".format(total))
