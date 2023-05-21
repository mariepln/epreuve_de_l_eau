# -*- coding: utf-8 -*-

import sys

string = sys.argv[1]
result = ""

def upper_char(char):
    if 'a' <= char <= 'z':
        return chr(ord(char) - 32)
    return char

def lower_char(char):
    if 'A' <= char <= 'Z':
        return chr(ord(char) + 32)
    return char

for i in range(len(string)):
    if i % 2 == 0: 
        result += upper_char(string[i])
    else:
        result += lower_char(string[i])

print(result)


    