# -*- coding: utf-8 -*-

for nb1 in range(100):
    for nb2 in range(100):
        combinaison = "{:02d} {:02d}".format(nb1, nb2)
        if nb1 != nb2: #ou for nb2 in range(nb1+1, 100)
            print(combinaison, end=", ")

print ("")