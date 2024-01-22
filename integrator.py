
print('|______________________________________________|')
print('On this platform you can do various operation \n______________________________________________\n1.playing tic tac toe game[1] \n______________________________________________\n2. play random_word_Choose game[2] \n______________________________________________\n3. Temperature converter[3] \n______________________________________________ \nEnter the numoer in front of each to choose one  ')
print('______________________________________________')
ask = input("what do you want to do ? ").strip().lower()
no_of_game_played = 0
from tic_tac_toe_project import play
if ask == '1':
    no_of_game_played += 1
    play()
    play_again = input("Do you want to play again ? (Yes/No ?").strip().upper()
    while play_again == "YES":
        no_of_game_played += 1
        play()
    else:
        print('You ve played '+str(no_of_game_played)+ ' times')
        print('Bye')
elif ask == "2":
    pass
elif ask == "3":
    pass
else:
    print(' i cant understand yah input !!! \n  Byyyyyyeeeeeeeeee')
