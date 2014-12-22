# -*  - coding: utf-8 -*- #============================================= #
# Program: ./p1.py #
# Author: Emil Gardström #
# Purpose: Does several problems from course Programmering 1 from Forsmarksskola #
# Action: Computes various numbers/results from an input number #
# Call: python ./p1.py functionnumber arg #
# Examples: python p1.py 1 1000 #
# Todo: * #
# Misc: 
#============================================
#



import sys

# Uppgift 1
# Kollar ett tals perfektion och printar svaret. Använd p = False för att endast få en matris över talets divisorer.
def uppgift1(number,p=True):
	
	i = 1#Iterator  
	table = []#Håller alla divisorer
	
	if number % 2 == 0: #Om numret är jämt 
		while i <= number/2: # Jämna tal har aldrig divisorer högre än deras rot, därför kan man sluta loopen när man kommer över den. Använd math.sqrt(number) om du vill endast veta att talet är perfekt eller inte
		
			if number % i == 0: # Om numret är delbart på i, t.ex 28(number) / 12(i), lägg till i(i) i matrisen
				table.append(i)
			i = i + 1 # öka i med 1

	else: #Denna körs enbart om talet är udda, och då det minsta udda mättade talet är 945, är det onödigt att göra ett test för både udda och jämna tal därför är funktionerna splittade. 
		if p:#Om utskrift
			print "Talet är ojämt därför är det högst osannolikt att det är perfekt"
		while i <= number/2: # Udda tal kan ha, om de inte är primtal, divisorer högre än deras rot. Men aldrig högre än deras hälft.

			if number % i == 0: # Samma som förut, om det udda numret är delbart på i, t. ex 9(number) / 3(i), lägg till i i(i) matrisen
				table.append(i)
			i += 1

	# Kollar om summan av matrisen—divisorerna —är mer, mindre eller lika med om p == True.
	if p:
		if not table.count(number / 2) and number%2 == 0:#Om talets hälft inte redan finns med i matrisen lägg till den
			table.append(number / 2)
		if sum(table) > number:#Om divisorernas summa är högre än number
			print "Talet %d är mättat\nSumman av divisorerna är %d" % (number, sum(table))
		elif sum(table) < number:#Om divisorernas summa är lägre än number
			print "Talet %d är omättat\nSumman av divisorerna är %d" % (number, sum(table))
		else: #Om summan inte är högre eller mindre än number
			print "Talet %d är perfekt" % number
		
	return table



# Uppgift 2
# Tar alla tal som är produkter av x och y under number. Om p = True skrivs progressionen ut.
def uppgift2(number,p=False, x = 3, y = 5): 
	rsum = 0 # totala summan.
  for i in range(1, number):
    if p: # Om utskrift OBS!! Tar väldigt längre tid med p = True
			print "i %d"%i
			print "rsum %d" % rsum
    if i % x:#Om talet gånger x är mindre än number. 
		  if i < number:
        rsum += (i)
		else:
      if i % y: #Om talet gånger y är mindre än number. Denna operation ska inte vara en if statement, då vissa y och x kan ha samma summa
        if i < number:
          rsum += (i)
	return rsum

#Beräknar Fibonanci serien upp till när nästa värde i serien är >n
def uppgift3(n):
	table = [1,1,0]
	track = sum(table)
	while table[2] < n:
		table[2] = table[0] + table[1]
		table[0] = table[1]
		table[1] = table[2]	
		track += table[2]
	return track
	print "0@%d I 1@%d I 2@%d" % (table[0],table[1],table[2])


if __name__ == "__main__":
  choose = -1
  x = ""
  arg = -1
  flag = False
  while True:
    try:
      choose = int(sys.argv[1])
    except:
      x = "No argument #"
      break
    if choose in [1,2,3]:
      try:
        arg = int(sys.argv[2])
        break
      except:
        x = "No arguments specified"
        flag = True

  if choose == 1 and not flag: 
    x = uppgift1(int(arg))
  if choose == 2 and not flag:
    x = uppgift2(int(arg),True)
  if choose == 3 and not flag:
    x = uppgift3(int(arg))
  print x
