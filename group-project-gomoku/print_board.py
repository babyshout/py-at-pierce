def print_board(board, board_size):
    # top side index print
    print("  ", end=" ")
    for i in range(board_size):
        if i < 9:
            print(i + 1, end="  ")
        else:
            print(i + 1, end=" ")
    print()

    # both side index and inner value(".", "*", "X", "O") print
    for i in range(board_size):
        if i < 9:
            print(i + 1, end="  ")
        else:
            print(i + 1, end=" ")
        for j in range(board_size):
            print(board[i][j], end="  ")
        if i < 9:
            print(i + 1, end="  ")
        else:
            print(i + 1, end=" ")
        print()

    # bottom side index print
    print("  ", end=" ")
    for i in range(board_size):
        if i < 9:
            print(i + 1, end="  ")
        else:
            print(i + 1, end=" ")
    print()
