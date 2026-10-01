class LoginClass:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        
users= []
try:
    with open("users.txt", "r") as file:
        for f in file:
            if f.strip() == "":
                continue
            data = f.strip().split("|")
            username = data[0].strip()
            password = data[1].strip()
            login = LoginClass(username, password)
            users.append(login) 
except FileNotFoundError:
    pass

while True:
    print("===Login System===")
    print("1. Register")
    print("2. Login")
    print("3. Exit")
    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Invalid choice. Please enter a number b/w 1-3.")
        continue
    match choice:
        case 1:
            found = False
            user_input = input("Enter your username: ")
            if user_input.strip() == "":
                print("Username cannot be empty.")
            else:
                for user in users:
                    if user_input == user.username:
                        found = True
                        break
                        
                if found == True:
                    print("Username already exist.")
                else:
                    password = input("Enter password: ")
                    if password.strip() == "":
                        print("Password cannot be empty.")
                    else:
                        login = LoginClass(user_input, password)
                        users.append(login)
                        with open("users.txt", "a") as file:
                            file.write(f"{login.username} | {login.password}\n")
                        print("Registered Successfully")

                        

        case 2:
            found = False
            user_input = input("Enter username: ")
            if user_input.strip() == "":
                print("Username cannot be empty.")
            else: 
                for user in users: 
                    
                    if user_input == user.username:
                        found = True
                        userpass = input("Enter password: ")
                        if userpass == user.password:
                            print("Login Successful")
                        elif userpass.strip() == "":
                            print("Password cannot be empty.")
                        else:
                            print("Wrong Password")

                if found == False:
                    print("Wrong Username")
        case 3:                
            break
