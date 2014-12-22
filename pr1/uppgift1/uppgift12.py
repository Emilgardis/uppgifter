# -*- coding: utf-8 -*-
#-----------------------------------------------------
# Program:  uppgift1.2.py
# Skapare:  Emil Gardström, FS14b
# Uppgift:  Uppgift 1.2
#             Tar framm summan av ett tals alla multipler upp till limit.
#    Call:  uppgift1.2.py limit [x,y]
#       ex. uppgift1.2.py 200
#       &>  Summan av alla multipliers av 3 & 5: 9168
#-----------------------------------------------------
# Init
import sys

#main()
def main(limit,x=3,y=5):
  """Genererar två listor med interval x och y, sedan summerar båda listor"""
  return (x,y),sum(set(range(0,limit,x) + range(0,limit,y)))



if __name__ == '__main__':
 print("Summan av alla multipliers av {0[0]} & {0[1]}: {1}".format(*main(int(sys.argv[1]))))
