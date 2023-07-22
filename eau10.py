# -*- coding: utf-8 -*-

import sys

args = sys.argv[1:]
last_arg = args[-1]
without_last_arg = args[:-1]

if last_arg in without_last_arg:
    for i in range(len(without_last_arg)):
        if last_arg == without_last_arg[i]:
            first_position = i
            print(first_position)
            break
else:
    print("-1")

    
        