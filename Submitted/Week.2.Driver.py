#class import
from Submitted.CheckingAccount import CheckingAccount

#create object
account1 = CheckingAccount("Jane Doe", "1234 Sesame St", 5678, 9098.76)

#credit
account1.AccountCredit(543.21)

#excessive debit
account1.AccountDebit(10243.19)

#debit
account1.AccountDebit(10.99)

#show balance for transactions
account1.ShowBalance()