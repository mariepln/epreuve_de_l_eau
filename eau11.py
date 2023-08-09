# -*- coding: utf-8 -*-

import sys

def find_min_abs ():
    difference = numbers_list[0] - numbers_list[1]
    min_abs = -difference if difference < 0 else difference
    for x in range(len(numbers_list)):
        for j in range(x+1, len(numbers_list)):
            difference = numbers_list[x] - numbers_list[j]
            abs_value = -difference if difference < 0 else difference
            if abs_value < min_abs:
                min_abs = abs_value
    return min_abs

numbers_list = [int(arg) for arg in sys.argv[1:]]

if len(numbers_list) < 2:
    print("error")
    sys.exit(1)

result = find_min_abs()
print(result)
            



