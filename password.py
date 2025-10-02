# random library used for randomizing characters
import random

#define variables that store each category of characters
char_lowlet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
               'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'] #26
char_upplet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
               'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'] #26
char_digits = ['0', '1', '2', '2', '3', '4', '5', '6', '7', '8', '9', ] #10
char_symbol = ['~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '=', '_',
              '+', '[', ']', "\\", ';', "'", ',', '.', '/', '{', '}', '|', ':',
              '"', '<', '>', "?", ' ',] #32
#list of variables for character pool
char_pool = [char_lowlet, char_upplet, char_digits, char_symbol]

# generates a random string of characters
# has two options, no specifications and with specifications
def generate_password(asklength, asklower, askupper, asknum, asksym):
    password = ""
    if asklower == None and askupper == None and asknum == None and asksym == None: # simple password generation
        for i in range(asklength):
            s = random.randint(0,3)
            if s == 0 or s == 1:
                s1 = 25
            elif s == 2:
                s1 = 10
            else:
                s1 = 31
            sb = random.randint(0,s1)
            password = password + char_pool[s][sb]
        return password
    elif asklower != None and askupper != None and asknum != None and asksym != None: #specified password generation
        z = True
        count = 0
        while z == True:
            s = random.randint(0, 3)
            if s == 0 and asklower != 0:
                s1 = 25
                asklower = asklower - 1
            elif s == 1 and askupper != 0:
                s1 = 25
                askupper = askupper - 1
            elif s == 2 and asknum != 0:
                s1 = 10
                asknum = asknum - 1
            elif s == 3 and asksym != 0:
                s1 = 31
                asksym = asksym - 1
            elif count == asklength:
                break
            else:
                continue

            sb = random.randint(0, s1)
            password = password + char_pool[s][sb]
            count = count + 1
        return password