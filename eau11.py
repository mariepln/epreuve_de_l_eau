# -*- coding: utf-8 -*-

import sys

def find_min_abs(numbers_list):
    min_abs = abs(numbers_list[0] - numbers_list[1])
    for x in range(len(numbers_list)):
        for j in range(x+1, len(numbers_list)):
            abs_value = abs(numbers_list[x] - numbers_list[j])
            if abs_value < min_abs:
                min_abs = abs_value
    return min_abs

numbers_list = [int(arg) for arg in sys.argv[1:]]

if len(numbers_list) < 2:
    print("error")
    sys.exit(1)

result = find_min_abs()
print(result)


            



