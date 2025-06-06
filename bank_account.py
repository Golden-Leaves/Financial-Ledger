import os.path
class Account():
    def __init__(self,name,password):
        self.name = name
        self.password = password
    def create_placeholder_file(self):
        with open("C:\\Users\\PC\\Desktop\\bank_account_pwd.txt", "a") as f:
            f.write("")
        with open("C:\\Users\\PC\\Desktop\\bank_account_username.txt", "a") as f:
            f.write("")
    def username_exists(self):
        with open("C:\\Users\\PC\\Desktop\\bank_account_username.txt", "r") as f:
            username = f.readline().strip()
        if username == "":
            print("No username found")
            username = input("Enter your username: ")
            with open("C:\\Users\\PC\\Desktop\\bank_account_username.txt", "w") as f:
                f.write(username + "\n")
            print(f"Here's your username {username} ")
        else:
            with open("C:\\Users\\PC\\Desktop\\bank_account_username.txt", "r") as f:
                username = f.readline().strip()
            print(f"Welcome {username}")
 
    def password_check(self):
        with open("C:\\Users\\PC\\Desktop\\bank_account_pwd.txt", "r") as f:
            line = f.readline().strip()
            if line == "":
                print("No password found")
                password = input("Enter a password for your bank account: ")
                with open("C:\\Users\\PC\\Desktop\\bank_account_pwd.txt", "w") as f:
                    f.write(password + "\n")
            else:
                print("Password found, enter the correct password")
                with open("C:\\Users\\PC\\Desktop\\bank_account_pwd.txt", "r") as f:
                    password = f.readline().strip()
                    counter = 0
                while True:
                  password_input = input()
                  print(f"Remaining tries {10 - counter}")
                  if password_input == password:
                    print("Password correct!")
                    return True
                  elif password_input != password and counter != 9:
                    print("Incorrect password")
                  elif counter == 9:
                    return False
                  counter += 1

                  
                
    def initialization(self):
        self.create_placeholder_file()
        self.username_exists()
        return self.password_check()
        

class BankAccount(Account):
    def __init__(self,name,password):
        super().__init__(name,password)
        first_run = os.path.exists("C:\\Users\\PC\\Desktop\\bank_account_balance.txt")
        if first_run == True:
          with open(r"C:\\Users\\PC\\Desktop\\bank_account_balance.txt","r") as f:
              line = f.readline()
              self.balance = int(line)
        elif first_run ==  False:
            self.balance = 0
            

    def view_balance(self):
        first_run = os.path.exists("C:\\Users\\PC\\Desktop\\bank_account_balance.txt")
        if first_run == True:
          with open(r"C:\\Users\\PC\\Desktop\\bank_account_balance.txt","r") as f:
            line = f.readline()
            balance = line.strip()
            balance = str(self.balance)
            print(f" Current balance: {balance}")
        elif first_run == False:
            print("You havent deposited money yet")
            
    def deposit_money(self):
        deposited = int(input("Enter the amount of money you would like to deposit: "))
        self.balance += deposited
        with open(r"C:\\Users\\PC\\Desktop\\bank_account_balance.txt","w") as f:
            f.write(str(deposited) + "\n")
        print(f"Deposited {deposited}, New balance: {self.balance}")
        
    def withdraw_money(self):
        withdraw = int(input("Enter the amount you would like to withdraw: "))
        self.balance -= withdraw
        print(f" Current balance: {self.balance}")
        with open(r"C:\\Users\\PC\\Desktop\\bank_account_balance.txt","w") as f:
            f.write(str(withdraw) + "\n")
            
    def possible_actions(self):
      while True:
        print("*****************************")
        print("1. View balance")
        print("2. Deposit money")
        print("3. Withdraw money")
        print("4. Quit the program")
        print("*****************************")
        user_input = int(input("Enter (1, 2, 3, 4) for the corresponding actions: "))
        if user_input == 1:
            self.view_balance()
        elif user_input == 2:
            self.deposit_money()
        elif user_input == 3:
            self.withdraw_money()
        elif user_input == 4:
            print("Exiting the program...")
            break
        else:
            print("Invalid input")
if __name__ == "__main__":
  acc_name = input("Type in '0' to start the program :")
  acc_pwd = input("Type in '0' to start the program :")
  bank_account = BankAccount(acc_name,acc_pwd)
  password_true = bank_account.initialization()
  if password_true == True:
    bank_account.possible_actions()
  elif password_true == False:
    print("Exceeded 10 passwords limit, terminating session...")
    