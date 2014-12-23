# -*- coding: utf-8 -*-
# -----------------------------------------------------
# Program:  uppgift23.py
# Skapare:  Emil Gardström, FS14b
# Uppgift:  Uppgift 2.3
#               Summan av allaprimtal under 2 miljoner
#    Call:  uppgift23.py arg1 arg2
# -----------------------------------------------------
#
import uppgift22


def main():
    sum = 0
    for i in uppgift22.primegen():  # Make generator. i is prime@cycle
        if i > 2e6:  # 2e6 = 2 million
            break
        sum += i
    print sum


if __name__ == '__main__':
    main()
