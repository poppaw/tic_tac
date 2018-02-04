import random
import os



def print_table(table):
    print(str(table[:3]) + "\n" + str(table[3:6]) + "\n" + str(table[6:9]))


def play():
    table = [ str(i) for i in range(1, 10)]
    user_numbers_chosen = []
    ai_numbers_chosen = []
    numbers_not_chosen = ['1', '2', '3', '4' ,'5' ,'6', '7', '8', '9']
    winning_combo = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9'], ['1', '4', '7'], 
                    ['2', '5', '8'], ['3', '6', '9'], ['1', '5', '9'], ['3', '5', '7']]
    print("Starting tic tac toe game!")
    print_table(table)
    player = random.randint(0, 1)
    if player == 0:
        user_sign = "x"
        ai_sign = "o"
    elif player == 1:
        user_sign = "o"
        ai_sign = "x"
    winning_game = False
    while not winning_game:
        choice = str(input("Choose number: "))
        if choice in table:
            user_numbers_chosen.append(choice)
            numbers_not_chosen.remove(choice)
            for i in range(len(table)):
                if table[i] == choice:
                    table[i] = user_sign
            os.system("clear")      
            print_table(table)
            for line in winning_combo:
                win = set(line) & set(user_numbers_chosen)
                if len(list(win)) == 3:
                    print("You won!")
                    winning_game = True
                    return winning_game
            if numbers_not_chosen == []:
                print("Nobody wins.")
                winning_game = True
                return winning_game
        print("Computers' turn.")
        for line in winning_combo:
            win_ai = set(line) & set(ai_numbers_chosen)
            win_user = set(line) & set(user_numbers_chosen)
            if len(list(win_ai)) == 2:
                move = list(set(line) - win_ai)
                correct_move = move[0]
                if correct_move not in numbers_not_chosen:
                    if len(list(win_user)) == 2:
                        move = list(set(line) - win_user)
                        correct_move = move[0]
                        if correct_move not in numbers_not_chosen:
                            ai_choice = random.choice(numbers_not_chosen)
                            break
                        else:
                            ai_choice = correct_move
                            break

                                
                else:
                    ai_choice = correct_move
                    break
                            
            elif len(list(win_user)) == 2 and not len(list(win_ai)) == 2:
                move = list(set(line) - win_user)
                correct_move = move[0]
                if correct_move not in numbers_not_chosen:
                    ai_choice = random.choice(numbers_not_chosen)
                    break
                else:
                    ai_choice = correct_move
                    break
            elif not len(list(win_user)) == 2 and not len(list(win_ai)) == 2:
                ai_choice = random.choice(numbers_not_chosen)
                
        
        if ai_choice in table:
            ai_numbers_chosen.append(ai_choice)
            numbers_not_chosen.remove(ai_choice)
            for i in range(len(table)):
                if table[i] == ai_choice:
                    table[i] = ai_sign
            os.system("clear")
            print_table(table)
            for line in winning_combo:
                win = set(line) & set(ai_numbers_chosen)
                if len(list(win)) == 3:
                    print("Compuer won!")
                    winning_game = True
                    return winning_game

    print("Game over. Therse no winner.")
    winning_game = True
    return winning_game


def main():
    esc = True
    while esc:
        on_off = input("To play press 'y' to quit press 'q': ")
        if on_off == "y":
            esc = True
        elif on_off == "q":
            esc = False
            return esc

        play()
        


if __name__ == '__main__':
    main()