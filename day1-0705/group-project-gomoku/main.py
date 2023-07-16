from print_board import *


def main():
    board_size: int = 9  # input("input board size")
    # board = [board_size][board_size]
    # board = []
    # for _ in range(board_size):
    #     row = [0] * board_size
    #     board.append(row)
    board = [["." for _ in range(board_size)] for _ in range(board_size)]

    # make this thing to init_board() function
    for row in range(9):
        for col in range(9):
            if row == 2 and col == 2:
                board[row][col] = "*"
            elif row == board_size - 3 and col == 2:
                board[row][col] = "*"
            elif row == 2 and col == board_size - 3:
                board[row][col] = "*"
            elif row == board_size - 3 and col == board_size - 3:
                board[row][col] = "*"
            # else:
            # board[row][col] = "."

    print_board(board, board_size)
    is_finished = True
    player = "X"
    opponent = "O"

    move_x = 0
    move_y = 0

    # start the game
    while is_finished:
        print_board(board, board_size)

        # move function start
        is_valid_move = False
        while not is_valid_move:
            try:
                move_x = int(input(f"player({player}), plz choose your move(x)")) - 1
                move_y = int(input(f"player({player}), plz choose your move(y)")) - 1

                if board[move_x][move_y] == player or board[move_x][move_y] == opponent:
                    is_valid_move = False
                elif move_x < 0 or move_x > board_size - 1:
                    is_valid_move = False
                elif move_y < 0 or move_y > board_size - 1:
                    is_valid_move = False
                else:
                    is_valid_move = True
                    break

                if not is_valid_move:
                    print(f"player({player}), your move is wrong. plz select valid move")

            except ValueError:
                is_valid_move = False

        # move player's stone
        board[move_x][move_y] = player
        # move function end

        # check the winning function start
        # function flow -> horizontal, vertical, 11 to 5, 1 to 7

        # if player(X or O) win, print winning comment and break the whole loop

        # change the player function start
        tmp = player
        player = opponent
        opponent = tmp
        # change the player function end


main()

# def print_board() :
#     for i in board_size:
#         for j in board_size:
#             print(board[i][j])
