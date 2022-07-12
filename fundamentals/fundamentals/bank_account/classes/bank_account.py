

class Bank_account:
    def __init__(self, int_rate = .01, balance = 0,):
        self.int_rate = int_rate 
        self.balance = balance

    def __repr__ (self):
        return repr(f"Your new balance is ${self.balance}")

    def deposit(self, amount):
        self.balance += amount
        print(f"Your new balance after deposit is: ${self.balance}")
        return self

    def withdraw(self, amount):
        self.balance -= amount
        if self.balance >= 0:
            
            print(f"Your new balance after withdrawal is: ${self.balance}")
        else:
            
            print("Insufficient funds: Charging a 5$ fee")
            self.balance -= 5
        return self
    
    def display_acc_info(self):
        print(f"Your balance is: ${self.balance}")
        return self

    def yield_interest(self):
        self.balance = self.balance + self.balance*self.int_rate
        print(f"You balance after interest is: ${self.balance}")
        return self

camden_acc = Bank_account(.05, 4000)

simon_acc = Bank_account(.01, 50000)

# camden_acc.deposit(50)
# camden_acc.deposit(100)
# camden_acc.deposit(200)
# camden_acc.withdraw(1000)
# camden_acc.yield_interest()
# camden_acc.display_acc_info()

# simon_acc.deposit(50)
# simon_acc.deposit(100)
# simon_acc.withdraw(10000)
# simon_acc.withdraw(10000)
# simon_acc.withdraw(500)
# simon_acc.withdraw(1)
# simon_acc.yield_interest()
# simon_acc.display_acc_info()

# camden_acc.deposit(10).deposit(10).deposit(100).deposit(1000).withdraw(2000).withdraw(100).yield_interest().display_acc_info()

# simon_acc.deposit(50).deposit(100).withdraw(10000).withdraw(10000).withdraw(500).withdraw(1).yield_interest().display_acc_info()

