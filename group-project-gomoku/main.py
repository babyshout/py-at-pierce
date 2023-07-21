from print_board import *


# main function start here
def main():
    # board_size defined (most go's board size is 19)
    board_size: int = 19  # input("input board size")

    # initialize the board, I tried many attempts
    # board = [board_size][board_size]
    # board = []
    # for _ in range(board_size):
    #     row = [0] * board_size
    #     board.append(row)
    # define the board and initialize inner value to "."
    board = [["." for _ in range(board_size)] for _ in range(board_size)]

    # should make this thing to init_board() function
    # init_board start here
    for row in range(board_size):
        # making the flower points
        for col in range(board_size):
            # 4th row
            if row == 3 and col == 3:
                board[row][col] = "*"
            elif row == 3 and col == 9:
                board[row][col] = "*"
            elif row == 3 and col == board_size - 4:
                board[row][col] = "*"

            # 10th row
            if row == 9 and col == 3:
                board[row][col] = "*"
            elif row == 9 and col == 9:
                board[row][col] = "*"
            elif row == 9 and col == board_size - 4:
                board[row][col] = "*"

            # 16th row
            elif row == board_size - 4 and col == 3:
                board[row][col] = "*"
            elif row == board_size - 4 and col == 9:
                board[row][col] = "*"
            elif row == board_size - 4 and col == board_size - 4:
                board[row][col] = "*"

            # else:
            # board[row][col] = "."
        # init_board end here

    # print_board() called. It is print the board
    print_board(board, board_size)
    # if game is finished -> escape the loop -> It is used as SWITCH( or FLAG)
    is_finished = True
    # define the 2 players symbol
    # 1st player's symbol = "X"
    player = "X"
    # 2nd player's symbol = "O"
    opponent = "O"

    # define the move_x, move_y. get the player's input and put that values into these
    move_x = 0
    move_y = 0

    # start the game
    while is_finished:
        # print_board()
        print_board(board, board_size)

        # move function start
        # 'is_valid_move is True' means that the player's move is valid
        is_valid_move = False
        while not is_valid_move:
            # exception handling start here
            try:
                move_y = int(input(f"player({player}), plz choose your move(AXIS x)")) - 1
                move_x = int(input(f"player({player}), plz choose your move(AXIS y)")) - 1

                if board[move_x][move_y] == player or board[move_x][move_y] == opponent:
                    is_valid_move = False
                # elif move_x < 0 or move_x > board_size - 1:
                # other language style if statement
                elif not 0 <= move_x < board_size + 1:
                    is_valid_move = False
                # elif move_y < 0 or move_y > board_size - 1:
                # other language style if statement
                elif not 0 <= move_y <= board_size:
                    is_valid_move = False
                # Q. + 1 to value and >= operator, which one is fast?
                else:
                    is_valid_move = True
                    break

                # can remove redundant

                if not is_valid_move:
                    print(f"player({player}), your move is wrong. plz select valid move")

            except ValueError:
                is_valid_move = False

        # move player's stone
        # insert player's stone where program got the input
        board[move_x][move_y] = player
        # move function end

        # check the winning function start
        # function flow -> horizontal, vertical, 1 to 7, 11 to 5
        # is_win is switch if "winner is there"
        is_win = False
        # directions will be used in for loop.
        # It is list what has the tuple.
        # Tuple is storage, its value is immutable
        directions = [(0, 1), (1, 0), (1, 1), (1, -1)]
        # BIG for loop. It check that there is winner
        # In this for loop, get the values from directions and insert into dr, dc
        for dr, dc in directions:
            # count var. if count == 5 -> winner
            count = 1
            # r = move_x
            r = move_x
            # c = move_y
            c = move_y
            # This while loop is not endless loop
            while True:
                # checking direction is + side
                r += dr
                c += dc
                # this loop will break here
                # if r or c is out of bounds -> break
                if not (0 <= r < board_size and 0 <= c < board_size):
                    break
                # if [r][c]'s value is NOT player -> break
                if board[r][c] != player:
                    break
                # if while not break -> count ++
                count += 1

            # reset the r, c to initial x, y
            r = move_x
            c = move_y

            while True:
                # checking through the - side
                r -= dr
                c -= dc
                # same as upper
                if not (0 <= r < board_size and 0 <= c < board_size):
                    break
                if board[r][c] != player:
                    break
                count += 1
            # if count is 5(5-in-row) -> win
            if count == 5:
                is_win = True
            # end of while loop

        # if win -> print the board, print the comment, break this while loop
        if is_win:
            print_board(board, board_size)
            print(f"{player}, you win!")
            break

        # if player(X or O) win, print winning comment and break the whole loop

        # change the player function start
        tmp = player
        player = opponent
        opponent = tmp
        # change the player function end

    # main function end here


# main function called here
main()

# def print_board() :
#     for i in board_size:
#         for j in board_size:
#             print(board[i][j])
