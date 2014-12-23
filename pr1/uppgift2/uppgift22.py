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
            # count is not in sieve therefore must be a prime
            yield count
            sieve[count**2] = [count]
            """
            Aristoteles sieve is made by crossing out composite numbers.
            The first unique composite number the new prime can make is the one
            where the factors are itself.

            Example.
            count -- 7, sieve -- {8: [2], 9: [3], 25: [5]}

            Since 7 is not in the dictionary it has to be a prime.
            To optimize, we don't add 14(7*2) to the dictionary, since this
            would result in a  uneeded double entry, since in some time, we will
            get to 14, and then both 7 and 2 will be 14.

                        sieve -- {14: [2],..., 14: [7]}

            To avoid this, we add 49(7*7) to the dictionary.
            """

        else:
            # count is in sieve, therefore it must be a composite.
            for p in sieve[count]:
                    sieve.setdefault(p + count, []).append(p)
                    """
                    setdefault makes so that the appended number is set with the
                    right number. This is the same as doing number = sieve.get
                    and then appending 'p + count : p' to sieve.


                    Example.
                    count -- 4, sieve -- {9: [3], 4: [2]}

                    Since 4 is in the dictionary it has to be a composite since
                    we know that all composite numbers are made of prime numbers
                    As the dictionary hints, 9 is 3*3, and 4 is 2*2.

                    Aristoteles sieve works by crossing out numbers that are
                    multiples of a prime, so we know that the next composite
                    to add to the dictionary would be 6 (2*3 or 2*2+2),
                    since 4 was already in the dictionary and 5 is a prime.
                    This is where setdefault comes in.
                    By adding 2 to 4, we get 6, which is a multiple of 2.

                        sieve.setdefault(p + count, []).append(p) simply states
                        add composite prime + count with translation multiple
                        to dictionary.

                    The dictionary now look like this:
                                sieve -- {9: [3], 4: [2], 6: [2]}
                    """
            del sieve[count]
        count += 1


def main():
    print next(islice(primegen(), 100001-1, None)),  # Return 100001th item of\
    # primegen generator
    print "is the 100001th prime"

if __name__ == '__main__':
    main()
