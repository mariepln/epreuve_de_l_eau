# -*- coding: utf-8 -*-

import sys

array = list(map(int, sys.argv[1:]))

def my_select_sort(array):
    for i in range (len(array)):
        min_nb = i
        for j in range (i + 1, len(array)):
            if array[j] < array[min_nb]:
                min_nb = j
        array[i], array[min_nb] = array[min_nb], array[i]
    return array

new_array = my_select_sort(array)
print(' '.join(map(str, new_array)))

