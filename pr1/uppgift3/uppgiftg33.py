# -*- coding: utf-8 -*-
#-----------------------------------------------------
# Program:  uppgiftg33.py 
# Skapare:  Emil Gardström, FS14b
# Uppgift:  Uppgift 3.3 (ProgB) (Gammal)
#             Syfte:När är lågenerglampa billigare
#             Anta K = Pris, E = Lampans Effekt i W, P är elpris i öre/kWh.
#           	K = E * H * P / 100,000
#             Anta:					Glödlampa	^	Lågenergilampa
#		          Effekt(W):	60				^	11		
#	          Livslängd(h):	1000			^	8000
# 		          Pris(kr):	5					^	60
#	        Input: 	Antal timmar per dag lampa lyser
#					        Elpris i öre per kWh(öre/kWh)
#	        Output:	Lågenergi är billigast efter x dagar.
#					Kostar ledPris för lågenergilampa och glodPris för glödlampa efter x dagar.
#    Call:  *.py arg1 arg2
#       ex. *.py x y
#       &>  x+y=z
#-----------------------------------------------------
# Init
import sys

def getInput():
  timmar = input("Antal timmar per dag lampan lyser? ")
  pris = input("Elpris i öre per kWh(öre/kWh)? ")
  return (timmar,pris)
#main()
def main(timmar,pris):
  
  while True:
      



if __name__ == '__main__':
 main(*getInput())
