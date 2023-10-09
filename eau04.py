# -*- coding: utf-8 -*-

import sys

#fonctions utilisées
def is_prime(number):
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

def find_next_prime(start_number):
    n = start_number + 1
    while not is_prime(n):
        n += 1
    return n

#parsing et gestion d'erreur
try:
    input_number = int(sys.argv[1])
    if input_number < 0:
        print("-1")
        sys.exit(1)
except ValueError:
    print("error")
    sys.exit(1)

if len(sys.argv) < 2:
    print("-1")
    sys.exit(1)

next_prime = find_next_prime(input_number)
print(next_prime)





