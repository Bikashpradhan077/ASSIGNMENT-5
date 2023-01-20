4#question solve
class Account:
    def __init__(self,title=None,balance=0):
        self.title = title
        self.balance = balance


class savingaccount(Account):
    def __init__(self, title=None, balance=0,interest=0):
        super().__init__()
        self.interest = interest
        print("Name : ",title)
        print("Balance : ",balance)
        print("Interest is : ",self.interest)


x =savingaccount("bikash",25000,4)