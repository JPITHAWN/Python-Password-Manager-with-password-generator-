#import json for data handling, and Fernet for data encryption
import json
from cryptography.fernet import Fernet

#Accont_class object for formatted storage
class Account_class:
    def __init__(self, website, username, password):
        self.website = website
        self.username = username
        self.password = password

file_path = "Passwords.txt"
Accounts = []
Accounts_dict = {}

# initialize_file, and reset_key are for setting up a new encryption key and new encrypted list
# load_key and fernet variable are always used, to load the encryption key to access list

# generate_personal_key
# key = Fernet.generate_key()
# with open ("secret.key", "wb") as file_key:
    #file_key.write(key)

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


# read_file function reads encrypted file, decrypts it using key which shows a json format
# json format is then read and converted into a dictionary, passed through the account_class object
# which is then put into the Accounts list for temporary storage
def read_file():
    global Accounts
    with open(file_path, "rb") as file:
        encrypted_file = file.read()
        decrypted_file = fernet.decrypt(encrypted_file).decode()
        Accounts_from_json = json.loads(decrypted_file)
    Accounts = [Account_class(json_dict["Website"], json_dict["Username"], json_dict["Password"]) for json_dict in Accounts_from_json]
    return Accounts

# rewrite_file function reads Accounts list, converts class objects into a dictionary
# then converted into json format to be encrypted using a key, which is then stored into the encrypted_file
def rewrite_file():
    global Accounts
    Accounts_dict = [{"Website" : acc.website, "Username" : acc.username, "Password" : acc.password} for acc in Accounts]
    json_passwords = json.dumps(Accounts_dict, indent=4)
    encrypted_file = fernet.encrypt(json_passwords.encode())
    with open(file_path, "wb") as file:
        file.write(encrypted_file)

# shows list of stored passwords
def show_password_list():
    read_file()
    counter = -1
    for acc in Accounts:
        counter += 1
        print(f"Website: {acc.website}\n Username: {acc.username}\n Password: {acc.password}\n")

# adds new password
def add_password(website, username, password):
    read_file()
    Accounts.append(Account_class(website, username, password))
    rewrite_file()
    print("It has been added!")

# edits existing password
def edit_password(website, username, password):
    read_file()
    for acc in Accounts:
        if acc.website == website and acc.username == username:
            acc.password = password
            rewrite_file()
            print("It has been edited!")
        else:
            print("error")

# deletes existing password
def delete_password(website, username):
        read_file()
        for acc in Accounts:
            if acc.website == website and acc.username == username:
                Accounts.remove(acc)
                rewrite_file()
                print("It has been deleted!")
