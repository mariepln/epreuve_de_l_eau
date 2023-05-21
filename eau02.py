# -*- coding: utf-8 -*-

#On veut parcourir chaque argument et les retranscrire en inversé

import sys

arguments = sys.argv[1:]
n = len(arguments)

for i in range(n - 1, -1, -1):
    print(arguments[i])
