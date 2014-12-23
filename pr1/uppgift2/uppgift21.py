# -*- coding: utf-8 -*-
# -----------------------------------------------------
# Program:  uppgift23.py
# Skapare:  Emil Gardström, FS14b
# Uppgift:  Uppgift 2.3
#           Hitta största palindrom tal med produkt av två 3-siffriga tal
#    Call:  python uppgift23.py
# -----------------------------------------------------
#


def fastpal(number):
    """Returns True if number is a palindrome.

    A palindrome is read the same forwards as backwards.
    matches the original.
    Keyword arguments:
    number -- number to be palindrome checked

    This is achieved with a simple slice reversal of the string equivalent of
    given number.
    """

    return str(number) == str(number)[::-1]


def main():
    n = [-1]  # contains highest yet multiple
    for i in range(1, 999):
        for k in range(1, 999):
            j = i * k  # Makes a temporary variable for palindrome checking.
            if fastpal(j) and j > n[0]:  # If palindrome and > than previous.
                n = [j, i, k]
    print "{} ({} * {}) is the highest possible palindrome consisting of 3 de"\
        "cimal places".format(n[0], n[1], n[2])
    return n[0]


if __name__ == '__main__':
    main()
