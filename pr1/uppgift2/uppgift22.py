# -*- coding: utf-8 -*-
# -----------------------------------------------------
# Program:  uppgift22.py
# Skapare:  Emil Gardström, FS14b
# Uppgift:  Uppgift 2.2
#               Vilket är det 10001:a primtalet
#    Call:  *.py arg1 arg2
#       ex. *.py x y
#       &>  x+y=z
# -----------------------------------------------------
# Init
from itertools import islice


def primegen():
    """docstring for primegen
    generates a iterator
    inspired by David Eppstein: http://code.activestate.com/recipes/117119/"""
    sieve = {}
    count = 2
    while True:
        if count not in sieve:
            # count is a prime, now yield and find multiple
            yield count
            sieve[count**2] = [count]

        else:
            # count is a composite, now
            for p in sieve[count]:
                    sieve.setdefault(p + count, []).append(p)
            del sieve[count]
        count += 1


def main():
    print next(islice(primegen(), 100001-1, None))


if __name__ == '__main__':
    main()
