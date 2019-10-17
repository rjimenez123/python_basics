def print_game(tic_tac_toe):
    print('  ' + '   '.join(['a', 'b', 'c']))

    for index, row in enumerate(tic_tac_toe, 1):
        print( str(index) + ' ' + ' | '.join(row) )
        if (index < 3):
            print('  ' + '  '.join(['-', '-', '-']))

def make_move(row, col, player, tic_tac_toe):
    col = ord(col) - ord('a')
    if player == 0:
        tic_tac_toe[row-1][col] = 'O'
    elif player == 1:
        tic_tac_toe[row-1][col] =  'X'

def marked_O(tic_tac_toe, row, col):
    col = ord(col) - ord('a')
    if (tic_tac_toe[row-1][col] == 'O'):
        return True
    else:
        return False

def marked_X(tic_tac_toe, row, col):
    col = ord(col) - ord('a')
    if (tic_tac_toe[row-1][col] == 'X'):
        return True
    else:
        return False

def is_blank(tic_tac_toe, row, col):
    col = ord(col) - ord('a')
    if (tic_tac_toe[row-1][col] == ' '):
        return True
    else:
        return False

def is_game_over(tic_tac_toe):
    count_Os = 0
    count_Xs = 0
    # cheking for the rows
    for row in range(3):
        for col in range(3):
            if (tic_tac_toe[row][col] == 'O'):
                count_Os += 1
            elif (tic_tac_toe[row][col] == 'X'):
                count_Xs += 1
        if (count_Os == 3 or count_Xs == 3):
            return True

    count_Os = 0
    count_Xs = 0
    # cheking for the cols
    for col in range(3):
        for row in range(3):
            if (tic_tac_toe[row][col] == 'O'):
                count_Os += 1
            elif (tic_tac_toe[row][col] == 'X'):
                count_Xs += 1
        if (count_Os == 3 or count_Xs == 3):
            return True

    count_Os = 0
    count_Xs = 0
    # cheking for the left diagonal
    row = 0
    col = 0
    while (row < 3):
        if (tic_tac_toe[row][col] == 'O'):
            count_Os += 1
        elif (tic_tac_toe[row][col] == 'X'):
            count_Xs += 1
        row += 1
        col += 1
    if (count_Os == 3 or count_Xs == 3):
        return True

    count_Os = 0
    count_Xs = 0
    # cheking for the right diagonal
    row = 0
    col = 2
    while (row < 3):
        if (tic_tac_toe[row][col] == 'O'):
            count_Os += 1
        elif (tic_tac_toe[row][col] == 'X'):
            count_Xs += 1
        row += 1
        col -= 1
    if (count_Os == 3 or count_Xs == 3):
        return True

    return False

#---------------------------------------------------------------------------------------------------------------

def main():
        tic_tac_toe = [ [' ', ' ', ' '],
                        [' ', ' ', ' '],
                        [' ', ' ', ' '] ]

        print("\t\t\tWelcome to TIC - TAC - TOE")
        print_game(tic_tac_toe)
        player = 1
        while (True):
            print("It's the turn of the player", player)
            row, col = input('Ingrese la posición en la que quiere hacer su jugada (por ejemplo: 2,b)\n').split(',')
            row = int(row)
            make_move(row, col, player, tic_tac_toe)
            print_game(tic_tac_toe)

            if (is_game_over(tic_tac_toe)):
                print("GAME OVER, Player", player, "won the game!")
                break
            else:
                print("THE GAME IS STILL ON!")

            player = 1 - player

#---------------------------------------------------------------------------------------------------------------
if __name__  == '__main__':
    main()
