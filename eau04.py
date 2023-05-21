# -*- coding: utf-8 -*-
import sys

n = int(sys.argv[1]) + 1

def is_prime(num):
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

while not is_prime(n):
    n += 1

print(n)




