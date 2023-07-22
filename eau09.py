# -*- coding: utf-8 -*-

import sys

arg_premier = int(sys.argv[1])
arg_second = int(sys.argv[2])

if arg_premier < arg_second:
    for i in range (arg_premier, arg_second):
        print(i, end=" ")
else:
    for i in range (arg_second, arg_premier):
        print(i, end=" ")

print("")