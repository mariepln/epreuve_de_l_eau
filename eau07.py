# -*- coding: utf-8 -*-

import sys

try: 
    string = sys.argv[1]
    result = ""

    def upper_char(char):
        if 'a' <= char <= 'z':
            return chr(ord(char) - 32)
        return char

    #méthode unpacking, extraire le premier mot de la chaîne, rassembler tous les mots restants dans une liste
    #découper la chaîne en une liste de mots, effectuer qu'une seule découpe
    while len(string):
        first_word, *rest_of_string = string.split(maxsplit=1)
        result += upper_char(first_word[0]) + first_word[1:] + " "
        string = rest_of_string[0] if rest_of_string else ""

    print(result.strip())
except:
    print("error")



