# -*- coding: utf-8 -*-
#-----------------------------------------------------
# Program:  uppgift11.py 
# Skapare:  Emil Gardström, FS14b
# Uppgift:  Uppgift 1.1
#             Tar fram om inskrivet svar är perfekt, mättat eller omättat. 
#    Call:  python ./uppgift11.py nummer
#       ex. python ./uppgift11.py 28
#       &>  Talet är perfekt
#       &>  Summan av dess divisorer är 28
#-----------------------------------------------------
# Init
import sys


#main()
def main(number,p=True):	
  """Delar upp ett tal till dess divisorer och ger dessa divisorer av dem."""
  table = []
  for i in range(1,number/2+1):
    if number % i == 0: # Om numret är delbart på i, t.ex 28(number) / 12(i), lägg till i i(i) matrisen
      table.append(i)
  return (table,number)

def perfectcheck(table,number):
  """ Kollar om summan av matrisen är mer, mindre eller lika med number."""
  if sum(table) > number:
    print "Talet %d är mättat\nSumman av divisorerna är %d" % (number, sum(table))
  elif sum(table) < number:
    print "Talet %d är omättat\nSumman av divisorerna är %d" % (number, sum(table))
  else:
    print "Talet %d är perfekt\nSumman av divisorerna är %d" % (number,sum(table)) 
if __name__ == '__main__':
  try:
    perfectcheck(*main(int(sys.argv[1])))
  except:
    print("Please input a number after filename!")
