game_board = [[0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]]
magic_square = [[8, 3, 4],
                [1, 5, 9],
                [6, 7, 2]]
human_list = []
computer_list = []

def checkRows(game_board):
    check = 0
    for i in range(3):
        for j in range(3):
            if game_board[i][j] == 0:
                return False
            else:
                check = check + game_board[i][j]
        if check != 15:
            return False    
        check = 0
    return True
def checkCols(game_board):
    check = 0
    for i in range(3):
        for j in range(3):
            if game_board[j][i] == 0:
                return False
            else:
                check = check + game_board[j][i]
        if check != 15:
            return False    
        check = 0
    return True
def checkDiagsleft(game_board):
    check = 0
    for i in range(3):
        if game_board[i][i] == 0:
            return False
        else:
            check = check + game_board[i][i]
    if check != 15:
        return False
    return True
def checkDiagsright(game_board):
    check = 0
    for i in range(0,3):
        j = 2 - i
        if game_board[i][j] == 0:
            return False
        else:
            check = check + game_board[i][j]
    if check != 15:
        return False    
    return True
def toss():
    coin = ['heads', 'tails']
    call = []
    call = input("choose heads or tails ")
    print()
    if random.choice(coin) == call:
        print("you won!")
    else:
        print("you lose you loser")
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
