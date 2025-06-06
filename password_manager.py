import vigenere
import os
#FIXME Note form future self: The eval() fucntion might be useful for the removal
key = "python"
def create_placeholders():
    with open(r"pwd_manager_master_pwd.txt", "w") as f:
        f.write("")
    with open(r"pwd_manager_passwords.txt", "w") as f:
        f.write("")
    with open(r"pwd_manager_names.txt", "w") as f:
        f.write("")
    with open(r"pwd_manager_application_or_website_names.txt", "w") as f:
        f.write("")
        
def master_password_setup():
    master_password = input("Setup your master password: ")
    with open(r"pwd_manager_master_pwd.txt", "w") as f:
        f.write(master_password + "\n")
    return True

def master_password_check():
    manager_passwords_exists = os.path.exists(r"pwd_manager_passwords.txt")
    with open(r"pwd_manager_master_pwd.txt","r") as f:
        no_master_pwd = f.readline().strip()
        
    if manager_passwords_exists and  not (no_master_pwd == " " or no_master_pwd == ""):
        while True:
            user_input = input("Enter the master password: ")
            with open(r"pwd_manager_master_pwd.txt", "r") as f:
                master_password = f.readline().strip()  
                if master_password == user_input:
                    return True
                else:
                    print("Incorrect password, please try again")
    else:
        print("Setting up a new master password...")
        print("Reopen the program once done with setup.")
        master_password_setup()
        
def add_info():
    username_info = input("Add the username associated with the account: ")
    password_info = input("Add the password associated with the account: ")
    website_application_info = input("Add the website/application name: ")
    encrypted_password_info = vigenere.encrypt(password_info,"python")
    with open(r"pwd_manager_passwords.txt", "a") as f:
        f.write(encrypted_password_info + "\n")
    with open(r"pwd_manager_names.txt", "a") as f:
        f.write(username_info + "\n")
    with open(r"pwd_manager_application_or_website_names.txt", "a") as f:
        f.write(website_application_info + "\n")




def view_info():
    with open(r"pwd_manager_names.txt", "r") as f:
        usernames = f.readlines()
    usernames = [username.strip() for username in usernames]
    if len(usernames) > 0:

        with open(r"pwd_manager_passwords.txt", "r") as f:
            passwords = f.readlines()
        decrypted_passwords = [vigenere.decrypt(password.strip(), key) for password in passwords]
        with open(r"pwd_manager_application_or_website_names.txt", "r") as f:
            wb_or_app_name = f.readlines()
        wb_or_app_name = [name.strip() for name in wb_or_app_name]
        for username, password, wb_or_app in zip(usernames, decrypted_passwords, wb_or_app_name):
            print(f"1. Username: {username} | Password: {password} | Website/Application: {wb_or_app}")
    else:
        print("No information found.")

def initialize():
    master_pwd_exists = os.path.exists(r"pwd_manager_master_pwd.txt")
    manager_passwords_exists = os.path.exists(r"pwd_manager_passwords.txt")
    manager_names_exists = os.path.exists(r"pwd_manager_names.txt")
    application_or_website_names_exists = os.path.exists(r"pwd_manager_application_or_website_names.txt")
    if not  (master_pwd_exists and manager_passwords_exists and manager_names_exists and application_or_website_names_exists):
        create_placeholders()
        return master_password_check()
    else: 
        return master_password_check()
    
# def other_options():
#     while True:
#         print("*******************************")
        
#         print("1.Remove information")
#         print("2.Return" + "\n")
        
#         print("*******************************")
#         user_input = input("Enter a number corresponding to an action: ")
#         if user_input == "1":
#             with open(r"pwd_manager_names.txt", "r") as f:
#                 usernames = f.readlines()
#                 usernames = [username.strip() for username in usernames]
#             with open(r"pwd_manager_passwords.txt", "r") as f:
#                 passwords = f.readlines()
#             decrypted_passwords = [vigenere.decrypt(password.strip(), key) for password in passwords]

#             with open(r"pwd_manager_application_or_website_names.txt", "r") as f:
#                 wb_or_app_name = f.readlines()
#                 wb_or_app_name = [name.strip() for name in wb_or_app_name]


#             Info_list = [(index,(username, password, wb_or_app)) for index,(username, password, wb_or_app) in enumerate(zip(usernames, decrypted_passwords, wb_or_app_name))]
#             for index,(username, password, wb_or_app) in enumerate(zip(usernames, decrypted_passwords, wb_or_app_name)):
#                 print(f"{index}. Username: {username} | Password: {password} | Website/Application: {wb_or_app}")

#             while True:
#                 print("Enter the information's number order to remove")
#                 print("The number order(s) should be seperated by commas (Example: 1, 2) (Also add a whitespace behind every comma)")
#                 try:
#                   remove_order = input()
#                   remove_order = [int(number) for number in remove_order.split(", ")]
#                   remove_info(remove_order)
#                 except ValueError as t:
#                     print("Invalid input")
#         elif user_input == "2":
#             return
#         else:
#             print("Invalid option. Please try again.")

# #Fixme at the top to fix
# def remove_info(indices):
#     with open(r"pwd_manager_names.txt", "r") as f:
#         usernames = f.readlines()
#         usernames = [username.strip() for username in usernames]


#     with open(r"pwd_manager_passwords.txt", "r") as f:
#         passwords = f.readlines()
#         passwords = [password.strip() for password in passwords]

#     with open(r"pwd_manager_application_or_website_names.txt", "r") as f:
#         wb_or_app_name = f.readlines()
#         wb_or_app_name = [line.strip() for line in wb_or_app_name]
#     info_list = [(index,(username, password, wb_or_app)) for index,(username, password, wb_or_app) in enumerate(zip(usernames, passwords, wb_or_app_name))]
#     reversed_indicies = sorted(indices, reverse = True)
#     for index in reversed_indicies:
#         index = int(index)
#         if index < len(info_list):
#           removed_info = info_list.pop(index)
#           removed_info = removed_info[1]
#           print(removed_info)
#           removed_username = str(removed_info[0])
#           removed_password = str(removed_info[1])
#           removed_platform = str(removed_info[2])
#           print(removed_username,removed_password,removed_platform)
#           with open(r"pwd_manager_names.txt", "r+") as f:
#             usernames = f.readlines()
#             usernames = [username.strip() for username in usernames if username == removed_username]
#             for username in usernames:
#                 if username != removed_username:
#                   f.write(username)


        


#           with open(r"pwd_manager_passwords.txt", "r+") as f:
#             passwords = f.readlines()
#             passwords = [password.strip() for password in passwords]
   
#           with open(r"pwd_manager_application_or_website_names.txt", "r+") as f:
#             wb_or_app_name = f.readlines()
#             wb_or_app_name = [line.strip() for line in wb_or_app_name]

#         else:
#             print("Invalid input, index exceeds limit")
        


def main():
    
    while True:
        print("*******************************")
        
        print("1.View information")
        print("2.Add information")
        print("3.Quit")
        
        print("*******************************")
        user_input = int(input("Enter a number corresponding to an action: "))
        if user_input == 1:
            view_info()
        elif user_input == 2:
            add_info()
        elif user_input == 3:
            return
        else:
            print("Invalid input")

if __name__ == "__main__":
    if initialize() == True: 
      main()
    
        
    