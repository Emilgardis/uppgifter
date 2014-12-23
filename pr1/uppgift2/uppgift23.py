# -*- coding: utf-8 -*-
# -----------------------------------------------------
# Program:  *.py
# Skapare:  Emil Gardström, FS14b
# Uppgift:  Uppgift *.*
#
#    Call:  *.py arg1 arg2
#       ex. *.py x y
#       &>  x+y=z
# -----------------------------------------------------
# Init
import uppgift22

uppgift22.main()


def main():
    sum = 0
    for i in uppgift22.primegen():
        if i > 2e6:
            break
        sum += i
    print sum


if __name__ == '__main__':
    main()
