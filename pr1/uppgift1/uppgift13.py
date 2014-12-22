# -*- coding: utf-8 -*-
#-----------------------------------------------------
# Program:  uppgift13.py 
# Skapare:  Emil Gardström, FS14b
# Uppgift:  Uppgift 1.3
#             Genererar summan av de jämna värdena i Fibon-
#           ancci serien som är under 4 miljoner(går att ändra)
#    Call:  *.py arg1 arg2
#       ex. *.py x y
#       &>  x+y=z
#-----------------------------------------------------
# Init
import sys

#main()
def main(lim=4000000):
  prev, cur = 0,1
  sumd2, temp = 0, 0
  while cur <= lim:
    temp = prev + cur
    prev = cur
    cur = temp
    if cur % 2 == 0:
      sumd2 += cur
  return sumd2

if __name__ == '__main__':
 print(main())
