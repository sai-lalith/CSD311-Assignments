import random
plays = ['X','O']
k = random.randint(0,2)
game_board = [["-", "-", "-"],
         ["-", "-", "-"],
         ["-", "-", "-"]]

magic_square = [[8, 3, 4],
                [1, 5, 9],
                [6, 7, 2]]

human_list = []
computer_list = []

def print_gameboard(game_board):
    print("   0, 1, 2")
    for count, row in enumerate(game_board):
        print(count, row)   

def pairs(list):
    pairs = []
    for i in range(len(list)):
        for j in range(len(list)):
            if i!=j:
                D = 15 - (list[i] + list[j])
                if D>0 and D<9:
                    pairs.append(D)
    return pairs

def human_input(magic_square, game_board,plays, human_list, computer_list):
    hrows = int(input("Enter the rows postion for your turn "))
    hcols = int(input("Enter the cols postion for your turn "))
    human_list.append(magic_square[hrows][hcols])
    magic_square[hrows][hcols] = 0
    game_board[hrows][hcols] = plays
    return game_board

pairs_sum = [] 
k = 0
     
def print_square(game_board):
    print("    0    1    2")
    for count, row in enumerate(game_board):
        print(count, row)


def computer_input(magic_square, game_board, plays,human_list, computer_list, k):
    pairs_sum = pairs(computer_list)
    for x in pairs_sum:
        for i in range(3):
            for j in range(3):
                if x == magic_square[i][j]:
                    computer_list.append(x)
                    game_board[i][j] = 2
              
                    k = 1
                    return game_board, k


    pairs_sum = pairs(human_list)
    for x in pairs_sum:
        for i in range(3):
            for j in range(3):
                if x == magic_square[i][j]:
                    computer_list.append(x)
                    magic_square[i][j] = 0
                    game_board[i][j] = plays
                    k = 0
                    return game_board, k

    while True:
            crows = random.randint(0,2)
            ccols = random.randint(0,2)
            if magic_square[crows][ccols] != 0:
                computer_list.append(magic_square[crows][ccols])
                game_board[crows][ccols] = plays
                magic_square[crows][ccols] = 0
                k = 0
                return game_board, k


def game(magic_square, game_board,plays, human_list, computer_list, k):
    print("WELCOME TO TIC-TAC-TOE")
    print_square(game_board)
    coin = ['heads', 'tails']
    call = []
    call = input("choose heads or tails: ")
    
    if random.choice(coin) == call:
        print("you won the toss")
        print("Want to play first? ")
        a= input("Y or N: ")
        if a == 'Y':
            while True:
                print("It's your turn, Enter the rows and columns coordinates: ")
                print()
                game_board = human_input(magic_square, game_board, plays[0], human_list, computer_list)
                print_gameboard(game_board)
                print("computer's turn")
                print()
                game_board, j = computer_input(magic_square, game_board,plays[1] ,human_list, computer_list, k)
                print_gameboard(game_board)
                if j != 0:
                    print("you lost the game.")
                    print("DO YOU WANT TO PLAY AGAIN?")
                    break
        else:
            print("You choose not to play first so, computer makes the first move")
            while True:
                print("computers turn")
                game_board = computer_input(magic_square, game_board,plays[0], human_list, computer_list,k)
                print_gameboard(game_board)
                print("human's turn")
                print()
                game_board, j = human_input(magic_square, game_board,plays[1], human_list, computer_list)
                print_gameboard(game_board)
                if j != 0:
                    print("you lost the game.")
                    print("DO YOU WANT TO PLAY AGAIN?")
                    break
    else:
        print("you lose the toss")
        print("computer will play first and you will be using o")
        while True:
                print("computers turn")
                game_board = computer_input(magic_square, game_board,plays[0], human_list, computer_list,k)
                print_gameboard(game_board)
                print("human's turn")
                print()
                game_board, j = human_input(magic_square, game_board,plays[1], human_list, computer_list)
                print_gameboard(game_board)
                if j != 0:
                    print("you lost the game.")
                    print("DO YOU WANT TO PLAY AGAIN?")
                    break
game(magic_square, game_board, plays,human_list, computer_list, k)       
