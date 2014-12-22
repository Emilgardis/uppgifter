#coding: utf-8

import os, sys
#översätter text till rövarspråket
def translate(filename, output=-1):
  """Translates regular swedish text to rovarspraket"""
  translationpack = 'bcdfghjklmnpqrstvwxz'
  translationpack +=  translationpack.upper()
  input = open(filename)
  if output == -1:
    os.path.splitext("filename")[0]
    base= os.path.splitext(os.path.basename(filename))
    target = open(base[0]+'_transl'+base[1],'w')
  else:
    target = open(output,'w')
  while not input.closed:
    char = input.read()

    for i in range(len(char)):
      if char[i] in translationpack:
        target.write(char[i] + 'o' + char[i].lower())

      else:
        target.write(char[i])


    input.close()
    target.close()
def lampef():
  H = float(raw_input('Timmar  tänd per dag? ')) 
  P = int(raw_input('Elpris i öre per kWh? '))
  E = (60.0,11.0)
  print "H: %d, P: %d, E1*H*P:%d" % (H,P,E[1]*H*P)
  k = [E[0] * P,E[1] * P]
  dagar = 41.0
  print k
    



        
  print sti(dagar)+" dagar krävs för att det ska bli effektivt"

if __name__ == "__main__":
  choose = -1
  output = ""
  arg = -1
  flag = False
  while True:
    try:
      choose = int(sys.argv[1])
    except:
      output = "No function called"
      break
    if choose in (1,2):
      try:
        arg = sys.argv[2]
        break
      except:
        output = "No arguments specified"
        flag = True
        break
      break
    break

  if choose == 1 and not flag: 
    output = translate(os.path.relpath(arg))

  #if choose == 2:
    #output = uppgift2(int(arg))
  if choose == 3:
    lampef()

