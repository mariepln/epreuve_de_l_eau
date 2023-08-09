# -*- coding: utf-8 -*-

import sys

arguments = sys.argv[1:]
n = len(arguments)

#fonctions utilisées
def reverse_arg(): 
    for i in range(n - 1, -1, -1):
        print(arguments[i])

#gestion erreur
if len(arguments) < 2:
    print("error")

#résultat
reverse_arg()

