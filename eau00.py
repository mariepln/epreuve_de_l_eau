# -*- coding: utf-8 -*-

def combinationNumber():
    for ch_one in range(10):
        for ch_two in range(10):
            for ch_three in range(10):
                combinaison = str(ch_one) + str(ch_two) + str(ch_three)
                if ch_one < ch_two < ch_three and ch_one != ch_three and ch_two != ch_three and ch_one != ch_two:
                    print(combinaison, end=", ")
    print("")

combinationNumber()
     





