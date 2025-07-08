class BankAccount:
    apr = 1.2
    
print(BankAccount.__dict__)

acc_1 = BankAccount()
acc_2 = BankAccount()
print(acc_1 is acc_2)
print(acc_1.__dict__ , acc_2.__dict__)
print(acc_1.apr, acc_2.apr)

BankAccount.account_type = 'Saving'

print(acc_1.account_type, acc_2.account_type)

acc_1.apr = 0
print(acc_1.__dict__, acc_2.__dict__)
print(acc_1.apr, acc_2.apr)
print(setattr(acc_2, 'apr', 10))
print(acc_1.apr, acc_2.apr)

acc_3 = BankAccount()

print(getattr(acc_3, 'apr'))


acc_1.bank = 'Acme saving and loans'
print(acc_1.__dict__)

print(BankAccount.__dict__)

class Programs():
    language = 'Python'
    
p = Programs()
print(p.__dict__)
p.__dict__['version']= '3.12'
print(p.__dict__)
print(p.version, p.language)