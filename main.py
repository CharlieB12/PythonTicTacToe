import time

boardId = ['', '', '', '', '', '', '', '', '']
score = 0
win = False
player1 = True


# function to display current board
def displayBoard(location, player):
    global boardId
    boardId[location] = player
    print('{0:<4} | {1:^4} | {2:>4}'.format(boardId[0], boardId[1], boardId[2]))
    print('-------------------')
    print('{0:<4} | {1:^4} | {2:>4}'.format(boardId[3], boardId[4], boardId[5]))
    print('-------------------')
    print('{0:<4} | {1:^4} | {2:>4}'.format(boardId[6], boardId[7], boardId[8]))
    print("\n")


# Checks the board for any winning orientation
def checkBoard():
    global win
    global boardId
    total = 0
    if boardId[0] == "O" and boardId[1] == 'O' and boardId[2] == 'O':
        print('Player 1 Wins!')
        win = True
    elif boardId[0] == "X" and boardId[1] == 'X' and boardId[2] == 'X':
        print('Player 2 Wins!')
        win = True
    elif boardId[3] == "O" and boardId[4] == 'O' and boardId[5] == 'O':
        print('Player 1 Wins!')
        win = True
    elif boardId[3] == "X" and boardId[4] == 'X' and boardId[5] == 'X':
        print('Player 2 Wins!')
        win = True
    elif boardId[6] == "O" and boardId[7] == 'O' and boardId[8] == 'O':
        print('Player 1 Wins!')
        win = True
    elif boardId[6] == "X" and boardId[7] == 'X' and boardId[8] == 'X':
        print('Player 2 Wins!')
        win = True
    elif boardId[0] == "O" and boardId[3] == 'O' and boardId[6] == 'O':
        print('Player 1 Wins!')
        win = True
    elif boardId[0] == "X" and boardId[3] == 'X' and boardId[6] == 'X':
        print('Player 2 Wins!')
        win = True
    elif boardId[1] == "O" and boardId[4] == 'O' and boardId[7] == 'O':
        print('Player 1 Wins!')
        win = True
    elif boardId[1] == "X" and boardId[4] == 'X' and boardId[7] == 'X':
        print('Player 2 Wins!')
        win = True
    elif boardId[2] == "O" and boardId[5] == 'O' and boardId[8] == 'O':
        print('Player 1 Wins!')
        win = True
    elif boardId[2] == "X" and boardId[5] == 'X' and boardId[8] == 'X':
        print('Player 2 Wins!')
        win = True
    elif boardId[0] == "O" and boardId[4] == 'O' and boardId[8] == 'O':
        print('Player 1 Wins!')
        win = True
    elif boardId[0] == "X" and boardId[4] == 'X' and boardId[8] == 'X':
        print('Player 2 Wins!')
        win = True
    elif boardId[2] == "O" and boardId[4] == 'O' and boardId[6] == 'O':
        print('Player 1 Wins!')
        win = True
    elif boardId[2] == "X" and boardId[4] == 'X' and boardId[6] == 'X':
        print('Player 2 Wins!')
        win = True

    # if the board is full and no winning orientations are found
    # a scratch is called and the board is reset
    else:
        for i in boardId:
            if i != "":
                total = total + 1
        if total == 9:
            print("Scratch!")
            print('\n')
            time.sleep(3)
            for i in range(len(boardId)):
                boardId[i] = ""
    return win


# Main board loop
playAgain = True
while playAgain:

    # sample board key
    print("Location Key:")
    print('{0:<4} | {1:^4} | {2:>4}'.format('0', '1', '2'))
    print('-------------------')
    print('{0:<4} | {1:^4} | {2:>4}'.format('3', '4', '5'))
    print('-------------------')
    print('{0:<4} | {1:^4} | {2:>4}'.format('6', '7', '8'))
    print("\n")

    # Brief pause before player choice options
    time.sleep(3)

    while not win:

        if player1:
            print("Player 1")

            loc = ""
            inRange = False
            isEmpty = False

            # if player input is within board parameters and the space is empty
            # an O is put at specified location
            while inRange is False or isEmpty is False:
                loc = input("Enter a location: ")
                loc = int(loc)
                if 0 <= loc <= 8:
                    inRange = True
                    if boardId[loc] == "":
                        isEmpty = True
                    else:
                        print('That space is already taken!')
                else:
                    print('Try again (0-8)')
            inp = "O"
            print("\n")
            player1 = False
        else:
            print("Player 2")

            loc = ""
            inRange = False
            isEmpty = False

            # if player input is within board parameters and the space is empty
            # an X is put at specified location
            while inRange is False or isEmpty is False:
                loc = input("Enter a location: ")
                loc = int(loc)
                if 0 <= loc <= 8:
                    inRange = True
                    if boardId[loc] == "":
                        isEmpty = True
                    else:
                        print("That space is already taken!")
                else:
                    print('Try again (0-8)')
            inp = 'X'
            print("\n")
            player1 = True
        # call to update board and check if there are any winning orientations
        displayBoard(loc, inp.upper())
        checkBoard()

    # Loop to ask if player wants to play again
    thru = False
    while not thru:
        choice = input("Do you want to play again? (y or n): ")
        if choice.lower() == 'n':
            thru = True
            playAgain = False
        elif choice.lower() == 'y':
            thru = True
            win = False
            boardId = ['', '', '', '', '', '', '', '', '']
            print('\n')
        else:
            print('Not a valid choice')
