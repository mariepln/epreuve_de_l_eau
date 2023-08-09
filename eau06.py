# -*- coding: utf-8 -*-

import sys

#fonctions utilisées
def upper_char(char):
    if 'a' <= char <= 'z':
        return chr(ord(char) - 32)
    return char

def lower_char(char):
    if 'A' <= char <= 'Z':
        return chr(ord(char) + 32)
    return char

def final(string):
    result = ""
    char_count = 0
    for i in range(len(string)):
        if string[i] != ' ':
            if char_count % 2 == 0: 
                result += upper_char(string[i])
            else:
                result += lower_char(string[i])
            char_count += 1
        else:
            result += ' '
    return result

#parsing
input_string = sys.argv[1]

#gestion d'erreur
if len(sys.argv) < 2:
    print("error")
    sys.exit(1)

if int(input_string):
    print("error")
    sys.exit(1)

#résolution
majuscule_sur_deux = final(input_string)

#affichage
print(majuscule_sur_deux)
