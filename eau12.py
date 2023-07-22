# -*- coding: utf-8 -*-

import sys

array = list(map(int, sys.argv[1:]))

def my_bubble_sort(array):
    for i in range (len(array)-1 , 0, -1):
        for j in range(i):
            if array[j] > array [j + 1]:
                array [j], array [j + 1] = array [j + 1], array [j]     
    return array

new_array = my_bubble_sort(array)
print(' '.join(map(str, new_array)))




