# -*- coding: utf-8 -*-

import sys

def my_bubble_sort(array):
    for i in range (len(array)-1 , 0, -1):
        for j in range(i):
            if array[j] > array [j + 1]:
                array [j], array [j + 1] = array [j + 1], array [j]     
    return array

if len(sys.argv) < 2:
    print("error")
    sys.exit(1)

number_list = list(map(int, sys.argv[1:]))

new_array = my_bubble_sort(number_list)
print(' '.join(map(str, new_array)))