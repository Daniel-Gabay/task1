board = ["-","-","-",
         "-","-","-",
         "-","-","-"]

Player1 = "x"
player2 = "0"
winner = None
gameRunning = True


# printing te game board
def printBoard (board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("----------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("----------")
    print(board[6] + " | " + board[7] + " | " + board[8])

#take player input 
def player1Input(board):
    inp = int(input("ps1-Enter a number 1-9: "))
    if inp >= 1 and inp <= 9 and board [inp-1] =="-":
        board[inp-1] = Player1
    else:
        print("Ooops player is already in that spot!")

def player2Input(board):
    inp = int(input("ps2-Enter a number 1-9: "))
    if inp >= 1 and inp <= 9 and board [inp-1] =="-":
        board[inp-1] = player2
    else:
        print("Ooops player is already in that spot!")

def win():

    if board [0] == board[1] and board [2] == board [1] and board[1]!= "-":
     print(f"win:{board[1]} ")
     
     return (False)
      
    elif board [3] == board[4] and board [5] == board [4] and board[4]!= "-":
     print(f"win:{board[4]} ") 
     
     return (False)
    
    elif board [6] == board[7] and board [8] == board [7] and board[7]!= "-":
     print(f"win:{board[7]} ") 
    
     return (False)
    
    elif board [6] == board[7] and board [8] == board [7] and board[7]!= "-":
     print(f"win:{board[7]} ") 
     
     return (False)
    
    else: 
      
       return (True)
     


#checkfor win or tie 

#switch the player 

#check for win or tie again 

while gameRunning:
    #reading player
    printBoard(board)
    player1Input(board)
    printBoard(board)
    gameRunning = win()
    player2Input(board)
    #win/loss
    gameRunning = win()
