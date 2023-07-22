# -*- coding: utf-8 -*-

import sys

string = sys.argv[1]
result = ""

def upper_char(char):
    if 'a' <= char <= 'z':
        return chr(ord(char) - 32)
    return char

while len(string):
    word, *rest = string.split(maxsplit=1)
    result += upper_char(word[0]) + word[1:] + " "
    string = rest[0] if rest else ""

print(result.strip())

