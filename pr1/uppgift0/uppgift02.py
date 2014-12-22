# -*- coding: utf-8 -*-
#-----------------------------------------------------
# Program: 
# Skapare:  Emil Gardström, FS14b
# Uppgift:  Uppgift *.*
#             Se main()
#    Call:  seconds.py [seconds]
#       ex. *.py 2000
#       &>  x+y=z
#-----------------------------------------------------
# Init
import sys

#main()
def main(seconds):
  """ Takes seconds and converts down to respective amount of 
  Days, hours, minutes and seconds in format "D:H:M:s", seconds has to be a float
  """
  # Sec is:
  # 1 day = 24h = 1440min = 86,400s
  # 1h = 60min = 3600s
  # 1 min = 60s
  # 1s = 1s (sic)
  days    = round(seconds/86400,3)
  hours   = round(seconds/3600,3)
  minutes = round(seconds/60,3)
  print("%G is ~equal to: %G days; %G hours; %G minutes; %G seconds") %(seconds,days,hours,minutes,seconds)
  return (days,hours,minutes,seconds)
if __name__ == '__main__':
 main(float(sys.argv[1]))
