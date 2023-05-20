#create CheckingAccount class

#include: name, address, account number, balance
#balance must be private to class using __

class CheckingAccount:
    def __init__(self, name, address, accountnumber, balance):
        self.__name=name
        self.__address=address
        self.__accountnumber=accountnumber
        self.__balance=balance
        
    #credit process
    def AccountCredit(self, amount):
        self.__balance=self.__balance+amount
        
    #debit process
    def AccountDebit(self, amount):
        if self.__balance<amount:
            print("Balance (${: .2f}) is insufficient. Debit for ${: .2f} unable to be completed.".format(self.__balance, amount))
        else:
            self.__balance=self.__balance-amount
                        
    #show balance
    def ShowBalance(self):
        print("Account {} current balance: ${:.2f}".format(self.__accountnumber, self.__balance))