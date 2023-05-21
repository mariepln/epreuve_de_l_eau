# -*- coding:utf-8 -*-

import sys

try:
    n = int(sys.argv[1])

    def fib(n):
        first_fib = 0
        second_fib = 1

        if n < 0:
            return -1

        if n == 0:
            return first_fib

        if n == 1:
            return second_fib

        count = 2 
        while count <= n:
            fib_n = first_fib + second_fib
            first_fib = second_fib
            second_fib = fib_n
            count += 1
        return fib_n

    if len(sys.argv) > 2:
        print("Veuillez entrer un seul argument")
    else:
        print(fib(n))
except:
    print("Erreur d'argument")





