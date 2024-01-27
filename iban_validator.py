
""""ibrzaztech"""
def iban_func(iban):
    global take_index
    iban_list, check, no_of_country_code = [], False, 0
    letter_digit = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                    'U', 'W', 'X', 'Y', 'Z']
    iban_list_2 = []
    " ".join(iban)
    sum = 0
    if iban.isalnum():
        for me in iban:
            iban_list.append(me)
        iban_list_2[-1:-4] = iban_list[0:4]
        iban_list_2[0:-4] = iban_list[4:]
        for i in iban_list_2:
            if not i.isdigit():
                no_of_country_code += 1
                for me in letter_digit:
                    if i == me:
                        take_index = 10 + iban_list_2.index(me)
                        iban_list_2[iban_list_2.index(i)] = take_index

        for i in iban_list_2:
            sum += int(i)
    if len(iban_list_2) != 6 and no_of_country_code != 4:
        check = True
    elif sum % 97 == 1:
        check = False


    if check:
        print("This IBAN is  Invalid")
    else:
        print("This IBAN is Valid")
iban = input("Input your IBAN : ").strip().upper()
iban_func(iban)