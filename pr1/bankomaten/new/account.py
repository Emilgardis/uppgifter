# -*- coding: utf-8 -*-
"""#-----------------------------------------------------
# Program:  *.py
# Skapare:  Emil Gardström, FS14b
# Uppgift:  Uppgift *.*
#             Förklaring av programmets betydelse
#    Call:  *.py arg1 arg2
#       ex. *.py x y
#       &>  x+y=
#-----------------------------------------------------
# Init """
import ConfigParser
import os
import base64
import hashlib
import random
ACCFILE = "accounts.txt"  # FIXME may be uneeded
VAULTFILE = "vault.txt"


class AccountHandler(object, ConfigParser.RawConfigParser):
    """AccountHandler is the container of all account values"""
    def __init__(self, account_file):
        super(AccountHandler, self).__init__()
        self.read(account_file)
        self.admin = False
    @classmethod
    def newAccount(self, ID, password, mode=1):
        """newAccount makes an account"""
        if self.has_section(self,ID):
            raise TypeError('ID: {} already exists')

        self.set(ID, 'salt', base64.b64encode(os.urandom(32)))
        self.set(ID, 'digest', hashlib.sha256('{}'.format(self.salt)
                                              + password).hexdigest())
        self.set(ID, 'type', mode)
        # TODO: Make money settable on new account
        self.set(ID, 'vmoney', hashlib.sha256('{}'.format(self.salt)
                                              + password
                                              + 0 + random.randint(10)))
        self.set(ID, 'history', 'Created;')
        return self
    @staticmethod
    def checkPassword(self, ID, password):
        """checks if password is correct"""
        return hashlib.sha256('{}'.format(self.salt)
                              + password).hexdigest() == self.get(ID, 'digest')

    def account(self, ID, password):
        """deprecated!! docstring for account"""
        if not self.has_section(ID):
            raise ValueError('ID: {} does not exist'.format(ID))
        if self.checkPassword(ID, password):
            pass


def main():
    acc = AccountHandler
    acc.newAccount('1234', '4321')
    print acc.get('1234', 'vmoney')
    print "Hello"


if __name__ == '__main__':
    main()
