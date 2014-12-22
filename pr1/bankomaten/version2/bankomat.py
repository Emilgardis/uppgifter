# -*- coding: utf-8 -*-
#-----------------------------------------------------
# Program:  *.py 
# Skapare:  Emil Gardström, FS14b
# Uppgift:  Uppgift *.*
#             Förklaring av programmets betydelse
#    Call:  *.py arg1 arg2
#       ex. *.py x y
#       &>  x+y=z
#-----------------------------------------------------
# Init
import sys
import math, time
import random, os
import base64, hashlib
import logging, getpass
import ju
ACCOUNTFILE = "accounts.txt"
clas Account(object):
  """Actual values of account
  """
  def __init__self, accountID, password, acc_file):
    "Initializer, sets the values to the values set in the acc_file"
    self.acc_file = acc_file
    self._accountID = str(accountID)
    self.digest = self.acc_file.get(self._accountID, 'digest')
    self._password = password
    self.salt = self.acc_file.get(self._accountID, 'salt')
    self.balance = self.acc_file.get(self._accountID, 'balance')
  
  @staticmethod
  def asList(value):
    "Make a string of each list member separated by new-carriage."
    value = filter(None, [x.strip() for x in value.splitlines()])
    return list(value)
  
  @staticmethod
  def list_toStr(value):
    """Same as asList(val) except does the opposite, takes a string
    and separates each section separated with new-carriage into a list"""
    return '\n'.join(value)
  
  @staticmethod
  def getDigest(password, salt):
    "Makes the digest of password and salt, used for password keeping"
    return hashlib.sha256('{}'.format(salt) + password).hexdigest()
  
  @staticmethod
  def listRemoveIndex(alist, index):
    del alist[index]
    return alist[:]
  @staticmethod
  def accountExist(account_ID):
    try:
      self.acc_file.items(account_ID)
      return True
    except ConfigParser.NoSectionError:
      return False
  def removeAccount(self):
    self.acc_file.remove(self.accountID)
  
  def isPassword(self, password):
    "Checks if digest of password and salt matches the orginalDigest"
    return self.getDigest(password, self.salt ) == self.digest
  
  def writeFile(self):
    "Saves acc_file, works outside of the class"
    with open(ACCOUNTFILE, 'wb') as configfile:
      self.acc_file.write(configfile)
  def getFile(self):
    return self.acc_file
  @property
  def salt(self):
    "self.salt get"
    return self.acc_file.get(self._accountID,'salt')

  @salt.setter  
  def salt(self, value):
    "self.salt setter"
    self.acc_file.set(self._accountID, 'salt', value)
  
  @property 
  def _digest(self):
    "self.digest getter"
    return self.acc_file.get(self._accountID, 'digest')
  @_digest.setter
  def _digest(self, value):
    "self.digest setter"
    self.acc_file.set(self._accountID, 'digest', value)

  @property
  def balance(self):
    "self.balance setter"
    return int(self.acc_file.get(self._accountID,'balance'))
  @balance.setter
  def balance(self, value,flag=True):
    "self.balance getter"
    if self.isPassword(self.password):
      self.acc_file.set(self._accountID, 'balance', value)
    else:
      return False

  @property
  def password(self):
    "self._password getter"
    return self._password
  @password.setter
  def password(self,value):
    "self._password setter"
    self._password = value
                                        
  @property
  def history(self):
    "self.history getter"
    return str(self.acc_file.get(self._accountID, 'history'))

  @history.setter
  def history(self, string):
    "self.history setter"
    self.acc_file.set(self._accountID, 'history', string)
   
    
  def updateHistoryX(self, string):
    """Deprecated. See log() instead.
    Updates history with current time and string"""
    if len(self.asList(self.history)) >10:
      self.history = self.list_toStr(self.listRemoveIndex(self.asList(self.history), 1))
    self.acc_file.set(self._accountID, 'history', self.history + '\n' + 
                time.strftime("%y-%m-%d-%H:%M:%S, {}".format(string)))

  def transferCashX(self, value, forced=False):
    """Deprecated, should be handled outside object.
    Updates the balance with value from  and updates history correctly"""
    if value < 0 and self.isPassword(self.password):
      if self.balance +  value < 0 and not forced:
        self.updateHistory("Error.!{:>8,}kr No funds Total:{:<,} kr".format(-value,self.balance))
        return False
      if self.balance + value >= 0 or forced:
        self.balance += value
        self.updateHistory("Withdrawal {:>6,}".format(-value,self.balance))
        return True
    elif value > 0 and self.isPassword(self.password) or forced:
      self.balance += value
      self.updateHistory("Deposit    {:>6,}".format(value,self.balance))
      return True
    return False
  

  @classmethod
  def New(cls, accountID, password, acc_file):
    """Called for new accounts
    Setups the config file for an new acccount"""
    cls.acc_file = acc_file
    
    cls.acc_file.read(ACCOUNTFILE)
    cls.acc_file.add_section(str(accountID))
    salt = base64.b64encode(os.urandom(32)) # Should not be needed but fixed a lot of problems, TODO


    cls._acc_file.set(str(accountID),    'salt',  salt)
    cls._acc_file.set(str(accountID),  'digest', cls.getDigest(password, salt))
    # assert cls.getDigest(password,salt) == cls.getDigest(password, salt)
    
    cls._acc_file.set(str(accountID), 'balance', 0)
    cls._acc_file.set(str(accountID), 'history', time.strftime("%d %b %Y %H:%M:%S, {}".format("Created account")))
    return cls(accountID, password, acc_file)

class Backend(object):
  """Handles account actions, give each argument a Account Class"""

#main()
def main():
  """main()""" 

def prompt():
  print"{:^}".format("bankomat.py - your bankomat of choice")
  while True:
    account = raw_input("enter account number: ")
    passwd = str(getpass.getpass("enter account password: "))
    try:
      acc = Account(account,passwd)
    except:
      print "Failed to fetch account"
      return False
    acc.transferCashX(raw_input("Amount to take"))
    acc.writeFile()

if __name__ == '__main__':
 main()
 prompt()
