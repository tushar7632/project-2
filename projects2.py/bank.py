
class Account:
    def __init__(self, balance,acc):
        self.balance = balance
        self.accountno = acc
    
        # debit method
    def debit(self, amount):
        self.balance -= amount
        print("Rs.", amount, "was debited")
        print("total balance = ", self.aayush())          
    def credit(self, amount):
        self.balance += amount
        print("Rs.", amount, "was credited")
        print("total balance = ", self.aayush())
    def aayush(self):
        return self.balance
                        
acc1 = Account(4000, 500)
acc1.debit(1000)
acc1.credit(500)
