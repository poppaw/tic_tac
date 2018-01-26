import random

def print_playing_board(lista):
        for item in lista:
            print('  '.join(item).center(40),'\n')
def main():
    #player1= input("Enter your name: ")
    players = ['player1', 'player2']
    begginer = random.randint(0,1)
    print("Start player: ", players[begginer], '\n')

    '''tic_tac = [[' ']*3]*3
    for item in tic_tac:
        print(''.join(item))'''

    tic = [str(i) for i in range(1,4)]
    tac = [str(i) for i in range(4,7)]
    toe = [str(i) for i in range(7,10)]
    tic_tac_toe = [tic, tac, toe]


    lista = tic_tac_toe
    print_playing_board(lista)
    
    

    answer = input ("Select space number to fill in \n")
    if answer in tic:
        for i in range(len(tic)): 
            if answer == tic[i]:
                tic_tac_toe[0][i] = "X"
    elif answer in tac:
        for i in range(len(tac)): 
            if answer == tac[i]:
                tic_tac_toe[1][i] = "X"
    elif answer in toe:
        for i in range(len(toe)): 
            if answer == toe[i]:
                tic_tac_toe[2][i] = "X"

    print_playing_board(tic_tac_toe)
    




main()
