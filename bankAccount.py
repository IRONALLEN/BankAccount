class BankAccount:
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        return self
        
    def withdraw(self, amount):
        if self.balance < amount:
            print(f"Insufficient Funds!, Balance is currently:{self.balance}. You withdraw request of {amount} can't be completed.")
        else:
            self.balance -= amount
            return self
    def display_account_info(self):
        print(f"Account info your current balance: ${self.balance}")

    def yield_interest(self):
        self.balance = self.balance + (self.balance * self.int_rate)
        print(f"you have an interest rate of {self.int_rate}, your new balance is: ${self.balance}")
        return self
jean_account = BankAccount(0.001, 2000)
chris_account = BankAccount(0.01, 5000)

jean_account.deposit(100).deposit(200).deposit(100).withdraw(1000).yield_interest().display_account_info()
chris_account.deposit(2900).deposit(1999).withdraw(800).withdraw(400).yield_interest().display_account_info()






















