#-*- coding: utf-8 -*-
# -----------------------------------------------------
# Program:  *.py
# Skapare:  Emil Gardström, FS14b
# Uppgift:  Uppgift *.*
#             Förklaring av programmets betydelse
#    Call:  *.py arg1 arg2
#       ex. *.py x y
#       &>  x+y=
# -----------------------------------------------------
#
import ConfigParser
import base64
import hashlib
import os
from Crypto.Cipher import ARC4

ACCLOC = "./accounts.txt"  # FIXME may be uneeded
VAULTFILE = "vault.txt"
CIPHER = ARC4.new('01231231')


class AccountFileHandler(object):

    """AccountHandler is the container of all account values"""

    def __init__(self, account_file):
        super(AccountFileHandler, self).__init__()
        self.parser = ConfigParser.RawConfigParser()
        self.parser.read(account_file)
        self.get = self.parser.get
        self.set = self.parser.set
        self.admin = False

    def new_account(self, ID, password, mode=1):
        """Return new account.

        When called, a unique `salt` is made. This `salt` is then used to create
        a salted hash on the `password`, a `digest`. The account starts with 0
        funds.

        Parameters
        ---------------------
        ID : str
            Unique account identifier, usually a 16 digit long str.
        password : str
            Password that is used to secure account.
        mode : int, optional
            Account type, ranges from 1 to 3.
            :1 - Debit card:
            :2 - Credit card:
            :3 - Charge card:

        Raises
        ---------------------
        TypeError
            If account already exist.

        Return
        ---------------------
        AccountHandler object
        """

        try:
            self.parser.has_section(ID)  # TODO make own exception
        except:
            raise TypeError('ID: {} already exists'.format(ID))
        self.parser.add_section(ID)
        self.set(ID, 'salt', base64.b64encode(os.urandom(32)))

        self.set(ID, 'digest', hashlib.sha256('{}'.format(
            self.get(ID, 'salt') + password)).hexdigest())

        self.set(ID, 'type', mode)

        # TODO: Make money settable on new account
        self.set(ID, 'vmoney', CIPHER.encrypt('182'))

        # example of stack implementation self.set(ID, 'stack', '')

        self.set(ID, 'history', 'Created;')
        return GetAccount(ACCLOC)

    @staticmethod
    def check_password(self, ID, password):
        """Check if password is correct.

        Digests `salt` with `password` and returns `True` if it matches
        `digest` in `ID`.

        Parameters
        ---------------------
        ID : str
            Unique account identifier, usually a 16 digit long str.
        password : str
            Password that has been set to secure account.

        Raises
        ---------------------
        # FIXME for raising exception id not existing.
        """

        digest = hashlib.sha256('{}'.format(
            self.get(ID, 'salt') +
            password).hexdigest())
        return digest == self.get(ID, 'digest')

    def get_account(self, ID):
        """Easy way of getting account details.

        Makes a dictionary of account with `ID`, so that one can easily display
        all variables. Usable when having a menu or similar.

        Only when you want pretty code, do not use when you for example want
        one variable only. Use get(ID, attrib) instead.
        """

        try:
            self.parser.has_section(ID)
        except:
            raise ValueError('ID: {} does not exist'.format(ID))
        # Makes list `flat`
        accinfo = [item
                   for sublist in self.parser.items(ID) for item in sublist]
        accinfoDict = dict(accinfo[i:i+2] for i in range(0, len(accinfo), 2))
        return accinfoDict

    def save(self, loc):
        """Save configfile"""
        with open(loc, 'wb') as configfile:
            self.write(configfile)


class GetAccount(AccountFileHandler, object):

    """Account getter"""

    def __init__(self, account_file):
        super(GetAccount, self).__init__(account_file)
        self._account = {}

        # account[id] setter
        for acc_ID in self.parser.sections():
            account_info = type(
                'Account',
                (AccountProperties,),
                self.get_account(acc_ID))
            self._account[acc_ID] = account_info()

    def __getitem__(self, key):
        # account[id] setter
        for acc_ID in self.parser.sections():
            account_info = type(
                'Account',
                (AccountProperties,),
                self.get_account(acc_ID))
            self._account[acc_ID] = account_info()
        return self._account[key]


class AccountProperties(object):

    """Account changer for type Account"""

    def __init__(self):
        pass

    def change_vmoney(self):
        print self.vmoney
        print "v"
