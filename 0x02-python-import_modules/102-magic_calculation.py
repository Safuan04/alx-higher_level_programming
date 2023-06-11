#!/usr/bin/python3
def magic_calculation(a, b):
    from magic_calculation_102 import add, sub
    calc = add(a, b)
    calcsub = sub(a, b)
    if a < b:
        for i in range(4, 6):
            calc = add(calc, i)
        return (calc)
    else:
        return(calcsub)
