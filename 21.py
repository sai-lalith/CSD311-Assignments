game_board = [[0, 1, 1],
            [3, 1, 0],
            [1, 0, 3]]


def check_win(game_board):
    #diagrow
    for i in range(3):
            if game_board[i][0] == game_board[i][1] == game_board[i][2] != 0 :
                print("winner -", game_board[i][0])
                return True
    
    #diagcol

    for j in range(3):
            if game_board[0][j] == game_board[1][j] == game_board[2][j] != 0:
                print("winner |", game_board[0][j])
                return True
    
                
        
    #diagleft
    k = 0
    for i in range(3):
         k = game_board[i][i] + k
    if k!= 0 and k== 3*game_board[0][0]:
        print("winner", game_board[0][0])
        return True

    #diagright
    x=0
    for i in range(3):
        j = 2 - i
        x = game_board[i][j] + x
    if x!=0 and x == 3*game_board[2][0]:
        print("winner /", game_board[2][0])
        return True

check_win(game_board)


