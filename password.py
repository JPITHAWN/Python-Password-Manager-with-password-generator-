import random

#define pool of characters
char_lowlet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
               'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'] #26
char_upplet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
               'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'] #26
char_digits = ['0', '1', '2', '2', '3', '4', '5', '6', '7', '8', '9', ] #10
char_symbol = ['~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '=', '_',
              '+', '[', ']', "\\", ';', "'", ',', '.', '/', '{', '}', '|', ':',
              '"', '<', '>', "?", ' ',] #32
char_pool = [char_lowlet, char_upplet, char_digits, char_symbol]
asklower, askupper, asknum, asksym = '','','',''

def generate_password():
    def nomods():
        password = ""
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

    def wmods(asklower, askupper, asknum, asksym):
        z = True
        count = 0
        password = ""
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


    a = True
    b = True
    invalid = "invalid input, try again"

    while a == True:
        try:
            asklength = int(input("How many characters do you want your password to have? (5 - 30) "))
            modlength = asklength
            if asklength > 30 or asklength < 5:
                print(invalid)
                continue
            else:
                break
        except Exception:
            print(invalid)
        finally:
            pass



    while a == True:
        askmods = input("Do you want more modifications? (y/n): ")
        if askmods == "n":
            while a == True:
                password = nomods()
                print('" '+ password + ' "')
                repeat = input("Generate again (enter) or type 'DONE': ")
                if repeat == "":
                    continue
                elif repeat == "DONE":
                    return password
                    a = False
                    break
                else:
                    print(invalid)
                    continue
                    
        elif askmods == "y":
            break
        else:
            print(invalid)
            continue


    while a == True:
        while b == True:
            try:
                asklower = int(input("How many lowercase letters do you want? (0 - " + str(modlength) + "): "))
                if asklower > modlength or asklower < 0:
                    print(invalid)
                    continue
                else:
                    modlength = modlength - asklower
                    break
            except Exception:
                print(invalid)
                continue
        while b == True:
            try:
                askupper = int(input("How many uppercase letters do you want? (0 - " + str(modlength) + "): "))
                if askupper > modlength or askupper < 0:
                    print(invalid)
                    continue
                else:
                    modlength = modlength - askupper
                    break
            except Exception:
                print(invalid)
                continue
        while b == True:
            try:
                asknum = int(input("How many numbers do you want? (0 - " + str(modlength) + "): "))
                if asknum > modlength or asknum < 0:
                    print(invalid)
                    continue
                else:
                    modlength = modlength - asknum
                    break
            except Exception:
                print(invalid)
                continue
        while b == True:
            try:
                asksym = int(input("How many symbols do you want? ("+str(modlength)+" - " + str(modlength) + "): "))
                if asksym != modlength:
                    print(invalid)
                    continue
                else:
                    modlength = modlength - asksym
                    break
            except Exception:
                print(invalid)
                continue
        break

    while a == True:
        password = wmods(asklower, askupper, asknum, asksym)
        print('" '+ password + ' "')
        repeat = input("Generate again (enter) or type 'DONE': ")
        if repeat == "":
            continue
        elif repeat == "DONE":
            return password
            a = False
            break
        else:
            print(invalid)
            continue