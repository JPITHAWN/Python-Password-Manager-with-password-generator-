# import actions for the actions, argparse for CLI, and generate_password for password generation
import actions, argparse
from password import generate_password

# entire argparse section is inside main() function, this is connected to the code below
def main():
    # parser variable stores umbrella for entire parser code
    # subparser variable gets defined as "commands" which is required as true
    parser = argparse.ArgumentParser(prog = "pass_manager", description = "An Encrypted Password Manager Program")
    subparsers = parser.add_subparsers(title = "Commands", dest="command", required=True)
    
    # argparse cli for adding a new password entry
    add_parser = subparsers.add_parser("add", help="Add a new password for a website/app")
    add_parser.add_argument("website", help = "Website name (ex., Github)")
    add_parser.add_argument("username", help = "Username/email for account")
    add_parser.add_argument("-p", "--password", help = "Create own password")
    add_parser.add_argument("-gen", "--generate", type = int, nargs="?", const=15, help = "Generate a randomized password of 15 characters unless length is specified")
    add_parser.add_argument("-u", "--uppercase", type = int, help= "Indicate how many uppercase letters" )
    add_parser.add_argument("-l", "--lowercase", type = int, help= "Indicate how many lowercase letters" )
    add_parser.add_argument("-n", "--number", type = int, help= "Indicate how many number characters" )
    add_parser.add_argument("-s", "--symbol", type = int, help= "Indicate how many symbols" )

    # argparse cli for editing an existing password entry
    edit_parser = subparsers.add_parser("edit", help="Edit an existing password/username/website")
    edit_parser.add_argument("website", help = "Website name (ex., Github)")
    edit_parser.add_argument("username", help = "Username/email for account")
    edit_parser.add_argument("-p", "--password", help = "Create own password")
    edit_parser.add_argument("-gen", "--generate", type = int, nargs="?", const=15, help = "Generate a randomized password of 15 characters unless length is specified")
    edit_parser.add_argument("-u", "--uppercase", type = int, help= "Indicate how many uppercase letters" )
    edit_parser.add_argument("-l", "--lowercase", type = int, help= "Indicate how many lowercase letters" )
    edit_parser.add_argument("-n", "--number", type = int, help= "Indicate how many number characters" )
    edit_parser.add_argument("-s", "--symbol", type = int, help= "Indicate how many symbols" )
    
    # argparse cli for deleting an existing password entry
    delete_parser = subparsers.add_parser("delete", help="Delete an existing username/website")
    delete_parser.add_argument("website", help = "Website name (ex., Github)")
    delete_parser.add_argument("username", help = "Username/email for account")

    # argparse cli for displaying the entire password list
    subparsers.add_parser("show", help="Display password list")
    
    #args variable is where we store sub_parser commands and required variable entries
    args = parser.parse_args()

    # if elif is to connect the argparse and the action functions
    if args.command == "add":
        if args.password:
            final_password = args.password
        elif args.generate:
            final_password = generate_password(
                asklength=args.generate, 
                asklower = args.lowercase, 
                askupper = args.uppercase, 
                asknum = args.number, 
                asksym = args.symbol
            )
        else:
            print("Error")
        actions.add_password(args.website, args.username, final_password)
    elif args.command == "edit":
        if args.password:
            final_password = args.password
        elif args.generate:
            final_password = generate_password(
                asklength = args.generate, 
                asklower = args.lowercase, 
                askupper = args.uppercase, 
                asknum = args.number, 
                asksym = args.symbol
            )
        else:
            print("Error")
        actions.edit_password(args.website, args.username, final_password)
    elif args.command == "delete":
        actions.delete_password(args.website, args.username)
    elif args.command == "show":
        actions.show_password_list()

# essentially means that main() runs if you initialize on this python file
if __name__== "__main__":
    main()

