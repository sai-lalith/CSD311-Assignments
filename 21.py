
game_board = [[1, 1, 1],
            [0, 3, 0],
            [0, 0, 6]]


def check_win():
	#diagrow
	
    for i in range(3):
            if game_board[i][0] == game_board[i][1] == game_board[i][2] != 0 :
            	print("winner -"+game[i][0])
            	break
            	 
              
    
    #diagcol
   
    #for i in range(3):
    for j in range(3):
            if game_board[0][j] == game_board[1][j] == game_board[2][j] != 0:
            	print("winner |"+ game_board[0][j])
            	break
                
        
    #diagleft
    k = 0
    for i in range(3):
         k = game_board[i][i] + k
    if k!= 0 and k== 3*game_board[0][0]:
	    print("winner \*"+ game_board[0][0])
	        
    
    #diagright
    
    
    for i in range(3):
        j = 2 - i
        x = game_board[i][j] + k
    if k!=0 and k == 3*game_board[0][2]:
    	print("winner /"+ game_board[0][2])
    	
        
        
    



