class BankAccount:
    def __init__(self, interest, balance):
        self.int_rate = interest
        self.acc_balance = balance
    
    def deposit(self, amount):
        self.acc_balance += amount
        return self

    def withdraw(self, amount):
        if 5 < self.acc_balance > 0:
            self.acc_balance -= amount
        else:
            print("Insufficient funds: charging a $5 fee")
            self.acc_balance -= 5
        return self

    def display_account_infor(self):
        print(f"Balance for: {self.acc_balance}")
        return self

    def yield_interest(self):
        self.acc_balance += self.acc_balance * self.int_rate
        print(f"New Balance with Interest: {self.acc_balance}")
        return self


Acc1 = BankAccount(.01, 1000)
Acc2 = BankAccount(.01, 3000)
Acc1.deposit(500).deposit(500).deposit(500).withdraw(1000).display_account_infor().yield_interest()
Acc2.deposit(1000).deposit(1000).withdraw(500).withdraw(500).withdraw(500).withdraw(500).display_account_infor().yield_interest()