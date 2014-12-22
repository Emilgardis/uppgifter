#-*- coding: utf-8 -*-

#Hitta största palindrom tal med produkt av två 3-siffriga tal
def reverse(orgnumber):
	tmpnumber,revnumber = orgnumber,0
	while tmpnumber > 0:
		revnumber = tmpnumber % 10 + revnumber * 10
		tmpnumber = tmpnumber / 10
	return revnumber


def fastpal(number):
	if str(number) == str(number)[::-1]:
		return True
	else:
		return False


def uppgift1():
  n = [-1]
  for i in range(1,999+1):
    for k in range(1,999+1):
      j = i * k
     # if i > 950 and k > 900 and k < 950:
      # print "%d * %d = %d" % (i, k, j)
      if fastpal(j) and j > n[0]:
        #print "%d is a palindrome" % j
        n = [j,i,k]
  print "%d (%d * %d) is the highest possible palindrome" % (n[0],n[1],n[2])
  return n[0]


uppgift1()
print fastpal(993 * 913)
def uppgift(summa):
  steg = [0,0,0]
  while summa % 500:
    if summa % 500:
      summa -= 500
      steg[0] += 1

  while summa % 200:
    if summa % 200:
      summa -= 200
      steg[1] += 1

  while summa % 100:
    if summa % 100:
      summa -= 100
      steg[2] += 1

  print "%dx500, %dx200, %dx100" % (steg[0],steg[1],steg[2])


print(uppgift(1000))

