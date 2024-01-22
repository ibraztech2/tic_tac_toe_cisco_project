#! i am called shabang
""""
 the first step is to list all the variable for  the game which are:
  no_of_play
  board (list of alll the 9 boxes)
  move_?( bool type ) to break out of the loop when either there is a winner or tie

 the second is to
"""
import sys
if __name__ == "__main__":
    print('dont do that')
    """ mamke the program to exit if someone tries to run is as stand alone"""
    sys.exit()



board = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]
move_list, no_of_play, move_list_0, play_on, bs, victor, continue_playing = [], 0, [], False, board, ['', False], True


def display_board(board_):
    print('+-----' * 3, end='+')
    print('')
    print('|     ' * 3, end='|')
    print('')
    for i in board_:
        for me in i:
            print('|  ' + str(me), end='  ')
        print('|', sep='')
        print('|     ' * 3, end='')
        print('|')
        print('+-----' * 3, end='+')
        print('')


def make_list_of_free_fields(board_free, user):
    # checks the input, and updates the board according to the user's decision.

    free_board = []
    for i in board_free:
        for me in i:
            if me != str:
                free_board.append(me)
            else:
                continue

        user_input_init = [(0, 0),
                           (0, 1),
                           (0, 2),
                           (1, 0),
                           (1, 1),
                           (1, 2),
                           (2, 0),
                           (2, 1),
                           (2, 2)]

        return user_input_init[user - 1]
    # this return  tuple which is used to update the user_input to the board


def victory_checker(board_vc):
    b_to_l = board_vc
    bk = [b_to_l[0][0], b_to_l[0][1], b_to_l[0][2], b_to_l[1][0], b_to_l[1][1], b_to_l[1][2], b_to_l[2][0],
          b_to_l[2][1], b_to_l[2][2], ]

    if bk[0] == bk[1] and bk[1] == bk[2]:
        return bk[0], True
    elif bk[0] == bk[3] and bk[3] == bk[6]:
        return bk[0], True
    elif bk[1] == bk[4] and bk[4] == bk[7]:
        return bk[1], True
    elif bk[2] == bk[5] and bk[5] == bk[8]:
        return bk[2], True
    elif bk[0] == bk[4] and bk[4] == bk[8]:
        return bk[0], True

    elif bk[2] == bk[4] and bk[4] == bk[6]:
        return bk[2], True

    elif bk[3] == bk[4] and bk[4] == bk[5]:
        return bk[3], True

    elif bk[6] == bk[7] and bk[7] == bk[8]:
        return bk[6], True

    elif no_of_play == 9:
        print('i am here')
        return 'tie', True
    else:
        return '', False


def winner(victor_w):
    if victor_w == 'X':
        return "you loose buddy !!!"
    elif victor_w == "O":
        return ' hurray i won buddy'
    elif victor_w == 'tie':
        return 'it is a tie'


def enter_move(board_u, move_list_u):
    global no_of_play, victor, continue_playing
    victor = victory_checker(board_u)
    if victor[1]:
        print(winner(victor[0]))
    if continue_playing:
        if no_of_play < 10 and not victor[1]:
            display_board(board_u)

            user_input = input('Enter your move :  ').strip()
            user_input = int(user_input)

            while user_input > 10 or user_input in move_list_u:
                if user_input > 10:
                    user_input = input('Please choose between 1 and 9 :')
                    user_input = int(user_input)

                if user_input in move_list:
                    user_input = input('choosen !!! please re Enter your move :')
                    user_input = int(user_input)

            move_list_u.append(user_input)
            user_input_init = make_list_of_free_fields(board_u, user_input)
            board_u[user_input_init[0]][user_input_init[1]] = 'O'
            if no_of_play == 9:
                continue_playing = False
                return None
            if not victor[1]:
                draw_move(board_u, move_list_u)
            else:
                print(str(victor[0]) + ' we are together')

    no_of_play += 1


from random import randint, randrange


def draw_move(board_c, move_list_c):
    global no_of_play, play_on, computer_move, victor
    victor = victory_checker(board_c)
    if victor[1]:
        print(winner(victor[0]))
    if not victor[1] and no_of_play < 10:
        if no_of_play <= 9:
            computer_move = randint(1, 9)

            while computer_move in move_list_c:
                computer_move = randint(1, 9)

        move_list_c.append(computer_move)
        computer_move_init = (make_list_of_free_fields(board_c, computer_move))
        board_c[computer_move_init[0]][computer_move_init[1]] = 'X'
        if not victor[1]:
            enter_move(board_c, move_list_c)

        no_of_play += 1
def play():
    first_player(board, move_list)

def first_player(board_f, move_list_f):
    game_starter = randrange(2)
    if game_starter == 1:
        draw_move(board_f, move_list_f)
    elif game_starter == 0:
        enter_move(board_f, move_list_f)
    display_board(board_f)

if __name__ == "__main__":
    print('i am a stand alone program')
    play()
else:
    print(' Na somebody end me oooo')
