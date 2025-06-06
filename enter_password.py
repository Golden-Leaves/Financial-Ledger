import math
#-----------------------------------------
#-----------------------------------------
Password = ""
# Function to set up the password
import math

# Global variable to store the password
Password = []

# Function to set up the password
def passwordSetup():
    global Password
    print("Enter your password below")
    password_setup = input()
    Password.append(password_setup)
    print(f"Password has been setup successfully, your password is now {Password}")

# Function to handle password setup decision
def set_up_password_decision():
    while True:
        print("New user detected, would you like to set up a password for this file? 'y' for Yes or 'n' for No")
        password_setup_choice = input().lower()
        if password_setup_choice == "y":
            passwordSetup()
            break
        elif password_setup_choice == "n":
            print("Proceeding without password...")
            break
        else:
            print("Please enter an appropriate input")

# Function to enter password
def enter_password(Password):
    while True:
        print("Please enter your password")
        user_input_password = input()
        if user_input_password == Password:
            safe_data()
            break
        else:
            print("Password incorrect, try again.")

# Function to check if the password has been set and proceed accordingly
def password_entered():
    global Password
    if Password == []:
        set_up_password_decision()
    elif Password:  # Check if a password is set
        enter_password()
    else:
        safe_data()

# Function to confirm successful data access
def safe_data():
    print("Password entered successfully!")

# Run the password check
password_entered()
Password = Password