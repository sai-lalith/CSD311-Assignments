game_board = [[3, 1, 1],
            [0, 3, 0],
            [0, 0, 3]]


def check_win(game_board):
    #diagrow
    for i in range(3):
            if game_board[i][0] == game_board[i][1] == game_board[i][2] != 0 :
                print("winner -", game_board[i][0])
    
    #diagcol

    for j in range(3):
            if game_board[0][j] == game_board[1][j] == game_board[2][j] != 0:
                print("winner |", game_board[0][j])
    
                
        
    #diagleft
    k = 0
    for i in range(3):
         k = game_board[i][i] + k
    if k!= 0 and k== 3*game_board[0][0]:
        print("winner", game_board[0][0])

    #diagright

    for i in range(3):
        j = 2 - i
        x = game_board[i][j] + k
    if k!=0 and k == 3*game_board[0][2]:
        print("winner /", game_board[0][2])

check_win(game_board)
