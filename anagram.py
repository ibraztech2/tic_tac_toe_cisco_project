alphabets = ['e', 'd', 'c', 'b', 'a', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',"v", 'u',
             'w', 'x', 'y', 'z']
place_value = 0
check = False
space = []


def encrypt_fun(string, alphabets):
    # encrypt = input("Enter word to encrypt").lower().split()
    encrypt_list = []

    for me in string:
        if me == " ":
            encrypt_list.append(" ")
        if me in alphabets:
            check = True
            string_index = alphabets.index(me)
            if string_index <= 20:
                encrypt_list.append(alphabets[5 + string_index])
            else:
                encrypt_list.append(alphabets[25 - string_index])
            print(string_index,end="   ")
    # print(encrypt_list)
    print("")
    for me in encrypt_list:
        print(me, end=" ")
    print("")


def dencrypt(string, alphabets):
    # encrypt = input("Enter word to encrypt").lower().split()
    encrypt_list = []

    for me in string:
        if me == " ":
            encrypt_list.append(" ")
        if me in alphabets:
            check = True

            string_index = alphabets.index(me)
            print(string_index,end='   ')
            if string_index <= 20:
                encrypt_list.append(alphabets[string_index - 5])
            else:
                if string_index > 20:
                    string_index = 0
                # print(string_index)
                # print(encrypt_list)
                # print(alphabets)
                encrypt_list.append(alphabets[(24 - string_index)])
    # print(encrypt_list)
    print(" ")
    for me in encrypt_list:
        print(me, end=" ")
    print("")


# dencrypt("n fr stgqj dcba", alphabets)
# dencrypt("n fr stgqj", alphabets)
# dencrypt("n fr stgqjn fr stgqj ajgxf ", alphabets)
print("encrypt")
encrypt_fun(str(alphabets),alphabets)
print("dencrypt")
dencrypt("f g h i j k l m n o p q r s t u w x y z e d c b a",alphabets)
# encrypt_fun("i am noble", alphabets)
# encrypt_fun("i am noble wxyz", alphabets)
