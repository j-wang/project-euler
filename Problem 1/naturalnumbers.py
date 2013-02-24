"""
File naturalnumbers.py
Version 1.0
Written by James Wang

Project Euler Question 1:
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. 
The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.

"""

def find_multiples(multiple, minimum, maximum):
    """Finds multiples of first argument, from min to max; returns list of multiples."""
    multlist = []
    
    for x in range(minimum, maximum):
        if x % multiple == 0:
            multlist.append(x)

    return multlist


def destroy_repeats(list1, list2):
    """Takes two ordered lists, returns list without repeats."""
    for x in range(0, len(list1) - 1):
        if list2.count(list1[x]) > 0:
            list2.remove(list1[x])

    list1.extend(list2)
    list1.sort()
    return list1


def main():

    print("Hello World")
    print(find_multiples(3, 0, 1000))
    print(find_multiples(5, 0, 1000))
    
    ans = destroy_repeats(find_multiples(3, 0, 1000), find_multiples(5, 0, 1000))
    print(sum(ans))
    
    
main()











