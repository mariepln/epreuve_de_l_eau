# -*- coding: utf-8 -*-

import sys

def min_max_numbers():
    first_arg = int(sys.argv[1])
    second_arg = int(sys.argv[2])
    if first_arg < second_arg:
        for i in range (first_arg, second_arg):
            print(i, end=" ")
    else:
        for i in range (second_arg, first_arg):
            print(i, end=" ")

    print("")

if len(sys.argv) < 2:
    print("error")
    sys.exit(1)

try:
    first_arg = int(sys.argv[1])
    second_arg = int(sys.argv[2])
except ValueError:
    print("error")
    sys.exit(1)

min_max_numbers()