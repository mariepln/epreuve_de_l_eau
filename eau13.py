# -*- coding: utf-8 -*-

import sys

def my_select_sort(array):
    for i in range (len(array)):
        min_nb = i
        for j in range (i + 1, len(array)):
            if array[j] < array[min_nb]:
                min_nb = j
        array[i], array[min_nb] = array[min_nb], array[i]
    return array

if len(sys.argv) < 2:
    print("error")
    sys.exit(1)

number_list = list(map(int, sys.argv[1:]))

new_array = my_select_sort(number_list)
print(' '.join(map(str, new_array)))