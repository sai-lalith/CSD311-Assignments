import random
plays = ['X','O']
k = random.randint(0,2)
square = [["-", "-", "-"],
         ["-", "-", "-"],
         ["-", "-", "-"]]

def print_square(square):
    print("0    1    2")
    for count, row in enumerate(square):
        print(count, row)
print_square(square)
def toss():
    coin = ['heads', 'tails']
    call = []
    call = input("choose heads or tails ")
    print()
    if random.choice(coin) == call:
        print("you won the toss")
        print("choose x or o")

    else:
        print("you lose the toss")
        print("computer will play first and you will be using x and  o")
