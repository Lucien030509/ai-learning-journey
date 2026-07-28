class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    def deposit(self, amount):
        self.balance = self.balance + amount
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance = self.balance - amount
            return True
        else:
            return False
            
account = BankAccount("Estella", 0)
print(f"{account.owner}‘s balance: {account.balance}")
friend_account = BankAccount("Alex", 100)
print(f"{friend_account.owner}‘s balance: {friend_account.balance}")
account.deposit(50)
print(f"{account.owner}‘s new balance: {account.balance}")
friend_account.deposit(25)
print(f"{friend_account.owner}'s new balance: {friend_account.balance}")
print(f"{account.owner}'s final balance: {account.balance}")
account.withdraw(20)
print(f"{account.owner}'s balance after withdrawal: {account.balance}")
withdrawal_success = account.withdraw(100)
if withdrawal_success:
    print("Withdrawal successful")
else:
    print("Insufficient funds for withdrawal")