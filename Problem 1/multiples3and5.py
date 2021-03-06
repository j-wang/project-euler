# multiples3and5.py
# Written by James Wang
# Project Euler Problem 1

# Find the sum of all the multiples of 3 or 5 below 1000.

ans = sum(n for n in range(1000) if n % 3 == 0 or n % 5 == 0)
print(ans)
