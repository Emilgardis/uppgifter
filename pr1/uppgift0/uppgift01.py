# -*- coding: utf-8 -*-
#-----------------------------------------------------
# Program:  uppgift0.1.py
# Skapare:  Emil Gardström, FS14b
# Uppgift:  Uppgift *.*
#             Summan, differensen, produckten och kvoten av två heltal.
#    Call: python uppgift0.1.py nummer1 nummer2
#         ex. python uppgift0.1.py 3 4
#         $>  3+4=7; 3-4=-1; 3*4=12; 3/4=0.75;
#-----------------------------------------------------
# Init
import sys

#main()
def main(a,b):
  """Få fram a+b, a-b, a*b och a/b
  och sätter in värdena på rätt plats.
  """
  print("{0[0]}+{0[1]}={1}; {0[0]}-{0[1]}={2}; {0[0]}*{0[1]}={3}; {0[0]}/{0[1]}={4};".format
  ([int(a),int(b)], int(a+b), int(a-b), int(a*b), a/float(b)))
  """
  str.format() ersätter bland annat "{0}" med ett sagt värde. Det motsvaras 
  av 'str() % variabel'
  T.ex "{0} {1} {2}".format(3,2,1) är samma som
  "%d %d %d" % [3, 2, 1] som blir "3 2 1"
  """
  
  

if __name__ == '__main__':
  main(float(sys.argv[1]),float(sys.argv[2]))
