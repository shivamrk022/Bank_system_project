class BankAccount:    #class name

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Deposited:", amount)       

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawn:", amount)
        else:
            print("Insufficient balance")

    def show_balance(self):
        print("Account Holder:", self.name)
        print("Balance:", self.balance)
        
acc1 = BankAccount("Shivam", 1000 )      #objects

acc1.deposit(6000)              #function call 
acc1.withdraw(3990)             #function call 
acc1.show_balance()              #function call 


