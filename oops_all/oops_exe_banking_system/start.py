import random

def generate_account_number():
    """function to generate a random account number"""
    return random.randint(10000, 99999)

class BankAccount:
    
    def __init__(self, account_holder):
        self.account_number = generate_account_number()
        self.account_holder = account_holder
        self.balance = 0
        
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited RS{amount}. new balance : RS{self.balance}")
            
        else:
            print("Deposit amount must be positive")
            
    
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdraw RS{amount}. new balance RS{self.balance}")
            
        else: 
            print("Insufficient balance or invalid withdraw")
            
    def display_details(self):
        print(f"Account Number: {self.account_number} , Account Holder: {self.account_holder}, Balance: {self.balance}")
        
    
class SavingAccount(BankAccount):
    def __init__(self, account_holder, mininum_balance):
        super().__init__(account_holder)
        self.minimun_balance = mininum_balance
        
    def withdraw(self, amount):
        if self.balance - amount < self.minimun_balance:
            print(f"Cannot withdraw, minimum balance requirement not met.")
        else:
            super.withdraw(amount)