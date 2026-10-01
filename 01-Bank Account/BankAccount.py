class BankAccount:
    # __init__: to assign initial values to object properties
    # self: a reference to current instance of class
    def __init__(self, name, accountNo, balance=0.0):
        self.name = name
        self.accountNo = accountNo
        self.balance = balance

    def deposit(self, amount):
        if(amount > 0):
            self.balance += amount
            print(f"${amount} deposited.")
    def withdraw(self, withdrawAmount):
        if(withdrawAmount > 0 and withdrawAmount <= self.balance):
            self.balance -= withdrawAmount
            print(f"Amount withdrawn: ${withdrawAmount:.2f}. Remaining balance: ${self.balance:.2f}. ")
        elif(withdrawAmount < 0):
            print("Enter positive amount")
        else:
            print("Insufficient Balance")       

    def check_balance(self):
        print("Current balance: ",self.balance)

    def account_info(self):
        print(self.name)
        print(self.accountNo)
        print(self.balance)


