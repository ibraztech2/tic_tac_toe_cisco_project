def encrypt_fun(string, alphabets):
    global encrypt_list
    # encrypt = input("Enter word to encrypt").lower().split()
    encrypt_list = []

    for me in string:
        if me == " ":
            encrypt_list.append(" ")
        if me in alphabets:
            check = True
            string_index = alphabets.index(me)
            if string_index <= 20:
                encrypt_list.append(alphabets[place_value + string_index])
            else:
                encrypt_list.append(alphabets[-(1 + string_index)])
            # print(f"\" " + str(string_index), end=f" {me}  ")

    # print(encrypt_list)
    print("")
    for me in encrypt_list:
        print(me, end="")
    print("")


check_index = ""


def dencrypt(string, alphabets):
    # encrypt = input("Enter word to encrypt").lower().split()
    global check_index
    encrypt_list = []

    for me in string:
        if me == " ":
            encrypt_list.append(" ")
        if me in alphabets:
            check = True
            string_index = alphabets.index(me)

            if string_index > 4:
                check_index = string_index - place_value
                encrypt_list.append(alphabets[check_index])
            else:
                encrypt_list.append(alphabets[-(1 + string_index)])
            # print(f"\" " + str(string_index), end=f" {me} ,++{check_index}  ,{alphabets[string_index]} ")
    print(" ")
    for me in encrypt_list:
        print(me, end="")
    print("")


def ask_crypt():
    ask = input("Do you want to encrypt :").lower().strip()
    if ask == "yes":
        plac_Valu_ = input("Place Value : ").strip()
        if plac_Valu_.isdigit() and plac_Valu_ == place_value:
            string = input("What do you want to encrypt :")
            encrypt_fun(string, alphabets)
            string2 = input("Do you wish to encrypt what you\"ve just encrypted").lower().strip()
            if string2 == "yes":
                dencrypt(str(encrypt_list), alphabets)
        else:
            print("wrong place value  !!!\nPlease try again !!!")
            ask_crypt()
    elif ask == "no":
        ask2 = input("Do you wish to dencrypt then :").strip().lower()
        if ask2 == " yes":
            string = input("What do you want to encrypt (yes/no):").strip().lower()
            dencrypt(string, alphabets)
            print("any")
        elif ask2 == "no":
            print("what do you want to do then ?")
            ask_crypt()
    else:
        print("please try again you \"ve entered Wrong input !!!")
        ask_crypt()


alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', "v",
             'u',
             'w', 'x', 'y', 'z']

place_value = 5
check = False
space = []
# encrypt_decrypt = ""


if __name__ == "__main__":
    ask_crypt()
