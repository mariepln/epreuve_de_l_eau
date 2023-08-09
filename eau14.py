# -*- coding: utf-8 -*-

import sys

def my_ascii_sort(arg_list):
    for i in range(len(arg_list)):
        min_index = i
        for j in range(i+1, len(arg_list)):
            k = 0
            while k < len(arg_list[min_index]) and k < len(arg_list[j]):
                if ord(arg_list[j][k]) < ord(arg_list[min_index][k]):
                    min_index = j
                    break
                elif ord(arg_list[j][k]) > ord(arg_list[min_index][k]):
                    break
                k += 1
            if k == len(arg_list[j]) and len(arg_list[j]) < len(arg_list[min_index]):
                min_index = j
        arg_list[i], arg_list[min_index] = arg_list[min_index], arg_list[i]
    return arg_list

if len(sys.argv) < 2:
    print("error")
    sys.exit(1)

arguments = sys.argv[1:]

new_arg_list = my_ascii_sort(arguments)
print (' '.join(new_arg_list))