# -*- coding: utf-8 -*-

import sys

try:

    first_arg = str(sys.argv[1])
    second_arg = str(sys.argv[2])

    def search_arg(second_arg, first_arg):
        second_len = len(second_arg)
        first_len = len(first_arg)

        for i in range(first_len - second_len + 1):
            similar_string = True
            for j in range(second_len):
                if first_arg[i + j] != second_arg[j]:
                    similar_string = False
                    break
            if similar_string:
                return True
        
        return False

    result = search_arg(second_arg, first_arg)
    print(result)

except:
    print("error")
