
print('|______________________________________________|')
print('On this platform you can do various operation \n______________________________________________\n1.playing tic tac toe game[1] \n______________________________________________\n2. play random_word_Choose game[2] \n______________________________________________\n3. Temperature converter[3] \n______________________________________________ \nEnter the numoer in front of each to choose one  ')
print('______________________________________________')
ask = input("what do you want to do ? ").strip().lower()
from tic_tac_toe_project import play
if ask == '1':
    play()
elif ask == "2":
    pass
elif ask == "3":
    pass
else:
    print(' i cant understand yah input !!! \n  Byyyyyyeeeeeeeeee')
