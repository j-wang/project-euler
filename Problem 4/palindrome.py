"""
File: palindrome.py
Version: 1.0 15 Dec 2012
Author: James Wang

Project Euler: Problem 4
A palindromic number reads the same both ways. The largest palindrome made from the product of two
2-digit numbers is 9009 = 91 99.

Find the largest palindrome made from the product of two 3-digit numbers.

"""
    
def reverse_number(num):
    """Reverses the order of a number and returns it."""
    temp = 0

    # Put num's digits into temp in reverse order
    while num > 0:
        temp *= 10
        temp += num % 10
        num = num / 10

    return temp


def is_palindrome(num):
    """Determines if a number is a palindrome. If it is, returns true."""
    if num == reverse_number(num):
        return True

    return False

    
def main():
    print(reverse_number(1002))

    print(is_palindrome(1001))
    print(is_palindrome(20409))
    

if __name__ == "__main__":
    main()









