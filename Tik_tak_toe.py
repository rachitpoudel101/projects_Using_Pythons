board = [ "__", "__", "__",
          "__", "__", "__",
          "__", "__", "__"]

current_Player ="X"
winner = None
gameRunning  = True

#printing the  the game board

def printBoard(board):
    print(board[0] + "|" + board[1]+ "|"+ board[2])
    print("---------")
    print(board[3] + "|" + board[4]+ "|"+ board[5])
    print("---------")
    print(board[6] + "|" + board[7]+ "|"+ board[8])
    
printBoard(board)