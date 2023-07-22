# -*- coding: utf-8 -*-

import sys

args = sys.argv[1:]

def chiffres_only(args):
    for chiffres in args:
        for c in chiffres:
            if  ord(c) < 48 or ord(c) > 57:
                return False
        return True

print(chiffres_only(args))


