# fibonacci.py
# Written by James Wang
# Project Euler Problem 2

# By considering the terms in the Fibonacci sequence whose values do
# not exceed four million, find the sum of the even-valued terms.

import math

def even_fib (maximum):
    """Generator producing even fib numbers up to max"""
    fib = 2
    i = 4  # from 2 (calced by 4), every 3rd fib # is even
    phi = (1+math.sqrt(5))/2

    while fib <= maximum:
        yield fib
        i += 3
        fib = round(math.pow(phi, i)/(phi + 2))

ans = sum(n for n in even_fib(4000000))
print (ans)










