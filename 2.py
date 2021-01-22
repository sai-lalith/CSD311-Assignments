import random
#initially the game board is empty and all the positions are declared as zero.

game_board = [[0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]]
# A sample magic square is declared for verifying the positions. 

magic_square = [[8, 3, 4],
                [1, 5, 9],
                [6, 7, 2]]
# two empty lists are declared for human and computer to keep track of their moves

human_list = []
computer_list = []

# check_win function checks and prints the winner
def check_win(game_board):
    # row
    for i in range(3):
            if game_board[i][0] == game_board[i][1] == game_board[i][2] != 0 :
                print("winner -", game_board[i][0])
                return True
    
    # column

    for j in range(3):
            if game_board[0][j] == game_board[1][j] == game_board[2][j] != 0:
                print("winner |", game_board[0][j])
                return True
               
        
    #left diagonal
    k = 0
    for i in range(3):
         k = game_board[i][i] + k
    if k!= 0 and k== 3*game_board[0][0]:
        print("winner", game_board[0][0])
        return True

    #right diagonal
    x=0
    for i in range(3):
        j = 2 - i
        x = game_board[i][j] + x
    if x!=0 and x == 3*game_board[2][0]:
        print("winner /", game_board[2][0])
        return True


# toss function decides whether human starts playing first or computer  

def toss():
    coin = ['heads', 'tails']
    call = []
    call = input("choose heads or tails ")
    print()
    if random.choice(coin) == call:
        print("you won the toss")
    else:
        print("you lose the toss")

# In human_input function the human player gives input as rows and columns in which he has to place his coin

def human_input(magic_square, game_board):
    hrows = input("Enter the rows postion for your turn ")
    hcols = input("Enter the cols postion for your turn ")
    human_list.append(magic_square[hrows][hcols])
    game_board[hrows][hcols] = 1
def computer_input(magic_square, game_board):
    if not computer_list:
        while True:
            crows = random.randint(0,2)
            ccols = random.randint(0,2)
            if magic_square[crows][ccols] not in human_list:
                break
