# -*- coding: utf-8 -*-

import sys

#fonctions utilisées
def is_prime(num):
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def find_next_prime(start):
    n = start + 1
    while not is_prime(n):
        n += 1
    return n

#parsing
input_number = int(sys.argv[1])

#gestion d'erreur
if len(sys.argv) < 2:
    print("-1")
    sys.exit(1)

if input_number < 0:
    print("-1")
    sys.exit(1)


next_prime = find_next_prime(input_number)
print(next_prime)





