def print_board(board, board_size):
    print("  ", end=" ")
    for i in range(board_size):
        if i < 9:
            print(i + 1, end="  ")
        else:
            print(i + 1, end=" ")
    print()
    for i in range(board_size):
        if i < 9:
            print(i + 1, end="  ")
        else:
            print(i + 1, end=" ")
        for j in range(board_size):
            print(board[i][j], end="  ")
        print()
