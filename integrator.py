
print('|______________________________________________|')
print('On this platform you can do various operation \n______________________________________________\n1.playing tic tac toe game[1] \n______________________________________________\n2. play random_word_Choose game[2] \n______________________________________________\n3. Temperature converter[3] \n______________________________________________ \nEnter the numoer in front of each to choose one  ')
print('______________________________________________')
ask = input("what do you want to do ? ").strip().lower()
play_Agin = True
from tic_tac_toe_project import play
if ask == '1':
    while play_Agin:
        play()
        play_again = input("Do you want to play again ? (Yes/No ?").strip().upper()
        if play_again == 'YES':
            play_Agin = True
        else:
            play_Agin = False
    else:
        print('Bye')
elif ask == "2":
    pass
elif ask == "3":
    pass
else:
    print(' i cant understand yah input !!! \n  Byyyyyyeeeeeeeeee')
