#!/bin/python3

import math

def help():
    print("USAGE");
    print("\t./108trigo fun a0 a1 a2....")
    print("DESCRIPTION")
    print('\tfun\tfunction to be applied, among at least "EXP", "COS", "SIN", "COSH" and "SINH"')
    print("\tai\tcoeficients of the matrix")

def is_square(nb):
        root = math.sqrt(nb)
        return root == math.trunc(root)

def error(argv):
    if len(argv) < 2:
        return 84
    elif not is_square(len(argv[1:])):
        return 84
    elif (argv[0] not in ("EXP", "COS", "SIN", "COSH", "SINH")):
        return 84
    for i in argv[1:]:
    	try:
    		int(i)
    	except (ValueError):
    		return 84
    return 0