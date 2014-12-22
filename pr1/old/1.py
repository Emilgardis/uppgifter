# -*- coding: utf-8 -*- #============================================= #
# Program: ./*.py #
# Author: Emil Gardström #
# Purpose: Does several problems from course Programmering 1 from Forsmarksskola #
# Action: Computes various numbers/results from an input number #
# Call: <program options, who starts it? cron?> #
# Examples: <How to run/use the program> #
# Todo: <Future updates etc> #
# Misc: <Text>
# Related bins: <Scripts/bins which are related> #
#============================================
#



import math, sys

# Uppgift 1
# Kollar ett tals perfektion och printar svaret. Använd p = False för att endast få en matris över talets divisorer.
def uppgift1(number,p=True):
	
	i = 1  
	table = []
	
	if number % 2 == 0: #Om numret är jämt 
		while i < math.sqrt(number)+1: # Jämna tal har aldrig divisorer högre än deras rot, därför kan man sluta loopen när man kommer över den.
			if number % i == 0: # Om numret är delbart på i, t.ex 28(number) / 12(i), lägg till i i(i) matrisen
				table.append(i)
			i = i + 1 # öka i med 1

	else: #Denna körs enbart om talet är udda, och då det minsta udda mättade talet är 945, är det onödigt att göra ett test för både udda och jämna tal. 
		if p:
			print "Talet är ojämt därför är det högst osannolikt att det är perfekt"
		while i < number/2: # Udda tal kan ha, om de inte är primtal, divisorer högre än deras rot. MEn aldrig högre än deras hälft.
		
			if number % i == 0: # Samma som förut, om det udda numret är delbart på i, t. ex 9(number) / 3(i), lägg till i i(i) matrisen
				table.append(i)
			i += 1
	# Kollar om summan av matrisen är mer, mindre eller lika med om p == True.
	if p:
		if not table.count(number / 2):
			table.append(number / 2)
		if sum(table) > number:
			print "Talet %d är mättat\nSumman av divisorerna är %d" % (number, sum(table))
		elif sum(table) < number:
			print "Talet %d är omättat\nSumman av divisorerna är %d" % (number, sum(table))
		elif p:
			print "Talet %d är perfekt" % number
		
	return table



# Uppgift 2
# Tar alla tal som är produkter av x och y under number tillsammans. Om p = True skrivs progressionen ut.
def uppgift2(number, x = 3, y = 5, p = True): 
  rsum = sum(set(list(range(0,number,x) + list(range(0,number,y))))) # totala summan.
	#Förklaring:  ppm range(0,number,x)
	#             
	return rsum

def uppgift3(n):
	table = [1,2,0]
	track = 0
	while table[2] < n:
		table[2] = table[0] + table[1]
		table[0] = table[1]
		table[1] = table[2]	
		track += table[2]
		print "0@%d I 1@%d I 2@%d" % (table[0],table[1],table[2])
	return track



choose = -1
while choose not in (1,2,3):
	if int(sys.argv[1]) in (1,2,3):
		choose = int(sys.argv[1])
	elif int(raw_input()) in (1,2,3):
		choose = int(raw_input())
	elif sys.argv[1] == '':
		print "Var god välj en funktion(1 - tals perfektion, 2 - funktion på x blablabla\n Funktion#  "
		while choose not in (1,2,3):
			choose = int(raw_input())
if choose == 1: 
	x = uppgift1(int(sys.argv[2]))
if choose == 2:
	x = uppgift2(int(sys.argv[2]))
if choose == 3:
	x = uppgift3(int(sys.argv[2]))
print x
