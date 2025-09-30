import password, actions

actions.Accounts = actions.read_file()

print("1. Add Password \n2. Edit Password \n3. Delete Password\n4. Check Password list\n5. Exit and Save Changes")
exit = False
while exit == False:
    action_type = int(input("Enter action 1-5: "))
    if action_type == 1:
        actions.add_password()
    elif action_type == 2:
        actions.edit_password()
    elif action_type == 3:
        actions.delete_password()
    elif action_type == 4:
        actions.show_password_list()
    elif action_type == 5:
        actions.rewrite_file()
        print("Program exited, thank you!")
        break
    