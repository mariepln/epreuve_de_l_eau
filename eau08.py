# -*- coding: utf-8 -*-

import sys

#fonctions utilisées
def chiffres_only(argument_list):
    for chiffres in argument_list:
        for c in chiffres:
            if  ord(c) < 48 or ord(c) > 57: #ou if not ('0' <= c <= '9'):
                return False
        return True
    
#gestion d'erreur
if len(sys.argv) < 2:
    print("error")
    sys.exit(1)

#parsing
arguments = sys.argv[1:]

#résolution
result = chiffres_only(arguments)

#affichage
print(result)


