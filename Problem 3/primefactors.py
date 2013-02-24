"""
File primefactors.py
Version 1.0, 12/9/2012
Written by James Wang

Project Euler, Problem 3:
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143?

"""

def is_prime(num):
    """Checks if a number is prime. Returns true or false."""
    index = 2

    # If 2 is not a factor, then there cannot be a factor > num/2, etc.
    while index <= num/index:
        if num % index == 0:
            return False
        else:
            index += 1

    return True


def prime_factors(num):
    """Finds and returns the prime factors of a number."""
    # untested
    factorslist = []
    index = 2

    while index < num:
        if num % index == 0:
            if is_prime(index):
                # If a prime number, add to list and run recursion on quotient
                factorslist.append(index)
                factorslist.extend(prime_factors(num/index))
            else:
                # If not a prime, go fetch prime numbers of divisor and quotient
                factorslist.extend(prime_factors(index))
                factorslist.extend(prime_factors(num/index))
        index += 1

    factorslist = list(set(factorslist))

    return factorslist


def largest_prime_factor(num):
    """Finds and returns the largest prime factor of a number."""
    index = 0

    while num - index > 0:
        if num % (num - index) == 0:
            if is_prime(num - index):
                return num - index
        index += 1


def fast_largest_prime_factor(num):
    """Finds and returns the largest prime factor of a number."""
    index = 2

    if is_prime(num):
        return num
    else:
        while index < num:
            if num % index == 0:
                if is_prime(num/index):
                    return num/index
            index += 1
        
        
def main():

    print(fast_largest_prime_factor(600851475143))
    print(fast_largest_prime_factor(11))
    print(fast_largest_prime_factor(121))
    
if __name__ == "__main__":
    main()










