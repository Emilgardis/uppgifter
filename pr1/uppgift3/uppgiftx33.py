#coding: utf-8
# Syfte:När är lågenerglampa billigare
# Anta K = Pris, E = Lampans Effekt i W, P är elpris i öre/kWh.
#	K = E * H * P / 100,000
# Anta:					Glödlampa	^	Lågenergilampa
#		 Effekt(W):	60				^	11		
#	Livslängd(h):	1000			^	8000
# 		Pris(kr):	5					^	60
#	Input: 	Antal timmar per dag lampa lyser
#					Elpris i öre per kWh(öre/kWh)
#	Output:	Lågenergi är billigast efter x dagar.
#					Kostar ledPris för lågenergilampa och glodPris för glödlampa efter x dagar.
def main(timmar,pris):
	ledPris, ledTid  = 60, 0
	glodPris, glodTid = 5, 0
	tid, dag = [0] * 2
	while ledPris > glodPris:
		dag+=1 # Addera dag.
		
		ledPris += 	(11 * timmar * pris/100000)
		glodPris +=	(60 * timmar * pris/100000)
		
		ledTid,glodTid = ledTid + timmar, glodTid + timmar
		
	if ledTid / 8000. > 1:
		ledPris += (tid/8000)*60
		ltid = 0 + (tid % 8000)
	if glodTid / 1000. > 1:
		glodTid= 0 + tid % 1000
		glodPris += (tid/1000)*5
	
	print("Efter %d dagar blir det billigare med lågenergilampa" % dag)
def getInput():
	timmar = input("Antal timmar per dag som lampan lyser? ")
	pris = input("Elpris i öre per kWh? ")
	return (timmar,pris)

main(*getInput())