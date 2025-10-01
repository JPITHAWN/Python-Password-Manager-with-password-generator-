
import password
import json
from cryptography.fernet import Fernet
from password import generate_password

class Account_class:
    def __init__(self, website, username, password):
        self.website = website
        self.username = username
        self.password = password
file_path = "Passwords.txt"
Accounts = []
Accounts_dict = {}

def load_key():
    with open("secret.key", "rb") as file_key:
        return file_key.read()

fernet = Fernet(load_key())

def initialize_file(file_path, key):
    fernet = Fernet(key)
    empty_list = json.dumps([]).encode()
    encrypted_data = fernet.encrypt(empty_list)
    
    with open(file_path, "wb") as f:
        f.write(encrypted_data)

def reset_key():
    key = open("secret.key", "rb").read()
    initialize_file("Passwords.txt", key)

def read_file():
    with open(file_path, "rb") as file:
        encrypted_file = file.read()
        decrypted_file = fernet.decrypt(encrypted_file).decode()
        Accounts_from_json = json.loads(decrypted_file)
    Accounts = [Account_class(json_dict["Website"], json_dict["Username"], json_dict["Password"]) for json_dict in Accounts_from_json]
    return Accounts

def rewrite_file():
    Accounts_dict = [{"Website" : acc.website, "Username" : acc.username, "Password" : acc.password} for acc in Accounts]
    json_passwords = json.dumps(Accounts_dict, indent=4)
    encrypted_file = fernet.encrypt(json_passwords.encode())
    with open(file_path, "wb") as file:
        file.write(encrypted_file)

def show_password_list():
    counter = -1
    for acc in Accounts:
        counter += 1
        print(f"{counter}. {acc.website}\n Username: {acc.username}\n Password: {acc.password}")

def add_password():
    AP_1 = input("Enter website name: ")
    AP_2 = input("Enter username: ")
    AP_4 = input("Generate password or make your own (A or B): ")
    while True:
        if AP_4 == "A":
            AP_3 = generate_password()
            break
        elif AP_4 == "B":
            AP_3 = input("Enter password: ")
            break
        else:
            pass
    Accounts.append(Account_class(AP_1, AP_2, AP_3))
    print("It has been added!")

def edit_password():
    show_password_list()
    EP_1 = int(input("which website do you want to edit (# only): "))
    print(f"Website: {Accounts[EP_1].website}\nCurrent Username: {Accounts[EP_1].username} \nCurrent Password: {Accounts[EP_1].password}")
    EP_2 = input("New username: ")
    EP_5 = input("Generate password or make your own (A or B): ")
    while True:
        if EP_5 == "A":
            EP_3 = generate_password()
            break
        elif EP_5 == "B":
            EP_3 = input("Enter password: ")
            break
        else:
            pass    
    EP_4 = Accounts[EP_1].website
    for acc in Accounts:
        if acc.website == EP_4:
            acc.username = EP_2
            acc.password = EP_3
            print("It has been edited!")
        else:
            print("error")
   
def delete_password():
    show_password_list()
    DP_1 = int(input("which password do you want to delete (# only): "))
    Accounts.remove(Accounts[DP_1])