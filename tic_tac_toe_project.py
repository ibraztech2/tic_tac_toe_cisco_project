from random import randrange
try:
    a, b, c, d, e, f, g, h, i = 1, 2, 3, 4, 5, 6, 7, 8, 9
    board = [[a, b, c],
             [d, e, f],
             [g, h, i]]
    board_1 = [[a, b, c],
             [d, e, f],
             [g, h, i]]
    bs = board
    move_list, no_of_play,move_list_1  = [], 0,[]



    def display_board(board):
        print('+-----' * 3, end='+')
        print('')
        print('|     ' * 3, end='|')
        print('')
        for i in board:
            for me in i:
                print('|  ' + str(me), end='  ')
            print('|', sep='')
            print('|     ' * 3, end='')
            print('|')
            print('+-----' * 3, end='+')
            print('')
            print('|     ' * 3, end='|')
            print('')

        # The function accepts one parameter containing the board's current status
        # and prints it out to the console.


    def enter_move(board, move_list):
        global no_of_play
        # display_board(board)
        while no_of_play < 9:
            display_board(board)
            user_input = int(input('Enter your move : '))

            while user_input > 9 or user_input in move_list:
                victory_holder = victory_checker(lis(board))
                if victory_holder[1]:
                    victory_for(victory_holder[0])
                    break
                if user_input > 9:
                    user_input = int(input('Plese choose between 1 and 9'))
                else:
                    user_input = int(input('choosen !!! please re Enter your move : '))
            else:
                move_list.append(user_input)

            user_tuple = (make_list_of_free_fields(board, user_input))
            board[user_tuple[0]][user_tuple[1]] = 'O'
            no_of_play += 1
            draw_move(board, move_list)
        # The function accepts the board's current status, asks the user about their move,


    def make_list_of_free_fields(board, user):
        # checks the input, and updates the board according to the user's decision.

        free_board = []
        for i in board:
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

        # The function browses the board and builds a list of all the free squares;
        # the list consists of tuples, while each tuple is a pair of row and column numbers.


    def victory_checker(bk):
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

        else:
            return 'tie', False


    def victory_for(sign):
        if sign == 'X':
            print('you lose buuddy ')
        elif sign == 'O':
            print('you win ')
        elif sign == 'tie':
            print('it\'s a tie buddy')
    #     The function analyzes the board 's statuus in order to check if
    #    the player using 'O's or "X"s has won the game
    def draw_move(board, move_list):
        global no_of_play
        while no_of_play < 9:
            compueter_move = randrange(1, 10)
            victory_holder = victory_checker(lis(board))
            if victory_holder[1]:
                victory_for(victory_holder[0])
                break
            while compueter_move in move_list:
                compueter_move = randrange(1, 10)
            else:
                move_list.append(compueter_move)
            compueter_move_init = (make_list_of_free_fields(board, compueter_move))
            board[compueter_move_init[0]][compueter_move_init[1]] = 'X'
            no_of_play += 1
            enter_move(board, move_list)
            victory_for(victory_holder[0])


    #     The functon draws the computer's move and updates the board.
    def first_player(board,move_list):
        game_starter = randrange(2)
        if game_starter == 1:
            draw_move(board, move_list)
        elif game_starter == 0:
            enter_move(board, move_list)
    def lis(board):
        bs = board
        bk = [bs[0][0], bs[0][1], bs[0][2], bs[1][0], bs[1][1], bs[1][2], bs[2][0], bs[2][1], bs[2][2], ]
        return bk


    first_player(board,move_list)
    display_board(board)
    play_again_str = input('Do you wanna play again  yes or no ').strip().upper()
    if play_again_str == 'YES':
        no_of_play = 0
        first_player(board_1,move_list_1)
    else:
        print('odabo !!! ')
except ValueError:
    print('please input integer and not character ')
except AttributeError:
    print('pleses input the correct the attribute ')
except:
    print('Well then i have tried my best but i dont seem to know what\'s wrong !!1')