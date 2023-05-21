# -*- coding: utf-8 -*-


for ch1 in range(10):
    for ch2 in range(10):
        for ch3 in range(10):
            combinaison = str(ch1) + str(ch2) + str(ch3)
            if ch1 < ch2 < ch3 and ch1 != ch3 and ch2 != ch3 and ch1 != ch2:
                print(combinaison, end=", ")
            
print("")




