board = []
boardSize = 6
for i in range(6):
    board[i] = '.'

def printBoard() :
    boardString = ''
    for i in board :
        boardString += i
    print(boardString)

printBoard()

move = input("Player X, what is your move? ")

i = 0
while i < 10 :
  print(i)
  i += 1
