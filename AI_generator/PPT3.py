from random import randint, choice, random

    
def jugadaPc():
        
    play = randint(0,2)
    if play == 'Piedra':
        user_choice = 0
    elif play == 'Papel':
        user_choice = 1
    elif play == 'Tijera':
        user_choice = 2
         
    return play
