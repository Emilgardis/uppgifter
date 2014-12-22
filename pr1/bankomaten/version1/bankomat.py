#-*- coding: utf-8 -*-
#-----------------------------------------------------
# Program:  bankomat.py
# Version:
# Creator:  Emil Gardström, FS14b
#    Task:  Uppgift 3
#    Call:  bankomat.py --gui
#       ex.
#       &>  x+y=z
#-----------------------------------------------------
# Init
import sys
import math, time
import ConfigParser
import random, os
import logging
import base64, hashlib
import pygame
import Pipeline
ACCOUNTFILE = 'accounts.txt'
class Unit(object):
  """The 'handler' of input and output, button presses and output,
  it is the ATM itself"""

  def __init__(self):
    "Set up all buttons"

class __futureFileHandler:
  """TODO; Replacement for ConfigParser. Can handle encrypted parts of files.

  Each user has a text portion in a file and each can be unlocked with the proper password, after this the file handler is able to change values.
  On exit the save() function is called whereupon the textfile is replaced with the new information.

  Order is like this
    handler = FileHandler("accounts.txt")>
        user = handler.getUser("password")>
            user.balance>

            user.history
            user._digest
            user._salt
            user._ID
            user._type"""

class Account(object):
  """A account with money, history and a security code"""

  def __init__(self, accountID, password, acc_file):
    "Initializer, sets the values to the values set in the acc_file"
    self._acc_file = acc_file
    self._accountID = str(accountID)
    self._digest = self._acc_file.get(self._accountID, 'digest')
    self._password = password
    self._salt = self._acc_file.get(self._accountID, 'salt')
    self._balance = self.acc_file.get(self._accountID, 'balance')
    self._type = self._acc_file.get(self._accID, 'type')
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

  def removeAccount(self):
    self.acc_file.remove(self.accountID)

  def isPassword(self, password):
    "Checks if digest of password and salt matches the orginalDigest"
    return self.getDigest(password, self._salt ) == self._digest

  def writeFile(self):
    "Saves acc_file, works outside of the class"
    with open(ACCOUNTFILE, 'wb') as configfile:
      self._acc_file.write(configfile)
  def getFile(self):
    return self._acc_file
  @property
  def salt(self):
    "self.salt get"
    return self._acc_file.get(self._accountID,'salt')

  @salt.setter
  def salt(self, value):
    "self.salt setter"
    self._acc_file.set(self._accountID, 'salt', value)

  @property
  def _digest(self):
    "self.digest getter"
    return self._acc_file.get(self._accountID, 'digest')
  @_digest.setter
  def _digest(self, value):
    "self.digest setter"
    self._acc_file.set(self._accountID, 'digest', value)

  @property
  def balance(self):
    "self.balance setter"
    return int(self._acc_file.get(self._accountID,'balance'))
  @balance.setter
  def balance(self, value,flag=True):
    "self.balance getter"
    if self.isPassword(self.password):
      self._acc_file.set(self._accountID, 'balance', value)
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
    return str(self._acc_file.get(self._accountID, 'history'))


  @history.setter
  def history(self, string):
    "self.history setter"
    self._acc_file.set(self._accountID, 'history', string)

  def updateHistoryX(self, string):
    """Deprecated. See log() instead.
    Updates history with current time and string"""
    if len(self.asList(self.history)) >10:
      self.history = self.list_toStr(self.listRemoveIndex(self.asList(self.history), 1))
    self._acc_file.set(self._accountID, 'history', self.history + '\n' +
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
  def New(cls, accountID, password, acc_file=None):
    """Called for new accounts
    Setups the config file for an new acccount"""
    if acc_file == None: # If no handler specified
      acc_file = ConfigParser.RawConfigParser()
    cls._acc_file = acc_file

    cls._acc_file.read(ACCOUNTFILE)
    cls._acc_file.add_section(str(accountID))
    salt = base64.b64encode(os.urandom(32)) # Should not be needed but fixed a lot of problems, TODO


    cls._acc_file.set(str(accountID),    'salt',  salt)
    cls._acc_file.set(str(accountID),  'digest', cls.getDigest(password, salt))
    # assert cls.getDigest(password,salt) == cls.getDigest(password, salt)

    cls._acc_file.set(str(accountID), 'balance', 0)
    cls._acc_file.set(str(accountID), 'history', time.strftime("%d %b %Y %H:%M:%S, {}".format("Created account")))
    return cls(accountID, password, acc_file)




#main()
def main():
  reader = ConfigParser.RawConfigParser()
  reader.read(ACCOUNTFILE)
  acc = Account("U3","ha", reader)
  acc.transferCashX(100,True)
  acc.transferCashX(-50)
  acc.writeFile()




if __name__ == '__main__':
  main()
