import sys
class Acount:
    Bank = "State Bank Of India"
    def _init_(self,Title=  None,Balance=0):
        self.Title = Title
        self.Balance = Balance
        print("Welcome to ",Acount.Bank)
        
    def deposite(self,deposit):
        self.Balance = self.Balance+deposit
        return  self.Balance

    def withdraw(self,withdraw):
        if self.Balance<withdraw:
            print("Inficient Balance You Can't Withdraw ")
            sys.exit()
        else:
            self.Balance = self.Balance-withdraw
            return self.Balance

    def get_balance(self):
        return self.Balance

class SavingAcount(Acount):
    def __init__(self, Title=None, Balance=0,inerestRate=0):
        super()._init_(Title, Balance)
        self.interestRate = inerestRate
        
    def interestAmount(self):
        self.interestRate = self.Balance*self.interestRate/100
        return self.interestRate


#Task-1 
a=SavingAcount("bikash",2000,5)
print("Initial balance: ",a.get_balance())
print()
#Task-2
a = SavingAcount("bikash",2000,5)
print("After Deposit : " ,a.deposite(500))
print()
#Task-3
a = SavingAcount("bikash",2000,5)
print("After Withdraw :",a.withdraw(500))
print()
#Task-4
a = SavingAcount("bikash",2000,5)
print("Interest amount is : ",a.interestAmount())