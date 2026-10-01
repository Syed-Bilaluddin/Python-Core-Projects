from BankAccount import BankAccount
accounts = []
with open("accounts.txt", "r") as file:
    for f in file:
        data = f.strip().split(",")
        if data[1].strip() == "Account Number":
            continue
        name = data[0].strip()
        accNo = int(data[1].strip())
        balance = float(data[2].strip())
        account = BankAccount(name, accNo, balance)
        accounts.append(account)
    # print(accounts[0].name)
    # print(accounts[0].accountNo)
    # print(accounts[0].balance)

    # accounts[0].deposit(500)
    # print(accounts[0].balance)
    
    print(len(accounts))

for acc in accounts:
    print(acc.name)
    print(acc.accountNo)
    print(acc.balance)

while True:
    print("====BANK===")
    print("1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Balance")
    print("5. Account Info")
    print("6. Exit")
    choice = int(input("Enter your choice: "))
    match choice:
        case 1:
            name = input("Enter your name: ")
            accNo = int(input("Enter account Number: "))
            account = BankAccount(name, accNo)
            accounts.append(account)
            print("Account created successfully")
        case 2:
            accNo = int(input("Enter account Number: "))
            for acc in accounts:
                if(accNo == acc.accountNo):
                    print("Account found")
                    dep = float(input("Enter Deposit amount: "))
                    acc.deposit(dep)
                    break
            else:
                print("Account not found")

        case 3:
            accNo = int(input("Enter account Number: "))
            for acc in accounts:
                if(accNo == acc.accountNo):
                    print("Account found")
                    wdraw = float(input("Enter withdraw Amount: "))
                    acc.withdraw(wdraw)
                    break               
            else:
                print("Account not found.")
        case 4:
            accNo = int(input("Enter account Number: "))
            for acc in accounts:
                if(accNo == acc.accountNo):
                    print("Account found")
                    acc.check_balance()
                    break
            else:
                print("Account not found")
        case 5:
            accNo = int(input("Enter account Number: "))
            for acc in accounts:
                if(accNo == acc.accountNo):
                    print("Account found")
                    acc.account_info()
        case 6:
            with open("accounts.txt", "w") as file:
                file.write("Name, Account Number, Balance")
                for acc in accounts:
                    file.write(f"{acc.name}, {acc.accountNo}, {acc.balance}\n")    
            break
        case _:
            print("Unknown")

        # name = data[0]
        # accNo = data[1]
        # balance = data[2]
        
        # print(f" {name}, {accNo}, {balance}")
    # ("Name, Account Number, Balance " \
    # "\n Bilal, 12345, 1000 " \
    # "\n Kamal, 23456, 2000 " \
    # "\n Jamal, 34567, 3000")
