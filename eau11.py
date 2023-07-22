# -*- coding: utf-8 -*-

import sys

numbers_list = sys.argv[1:]

min_abs = float('inf')  

for x in range(len(numbers_list)):
    for j in range(x+1, len(numbers_list)):
        difference = numbers_list[x] - numbers_list[j]
        abs_value = -difference if difference < 0 else difference
        if abs_value < min_abs:
            min_abs = abs_value

print(min_abs)

                


