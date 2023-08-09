# -*- coding: utf-8 -*-

def combinationNumber ():
    for first_nb in range(100):
        for second_nb in range(100):
            combinaison = "{:02d} {:02d}".format(first_nb, second_nb)
            if first_nb != second_nb: #ou for second_nb in range(nb1+1, 100)
                print(combinaison, end=", ")
    print ("")

combinationNumber()

