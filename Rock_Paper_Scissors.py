# THis python file simulates the game of rock paper scissors. Three tries allowed per person
# Rules:
# Rock breaks scissors. Rock Wins
# Scissor cuts papaer. Scissor wins
# Paper covers rock. Paper wins
# Both same item chosen. Continue
from random import randint
base_choice=('Rocks', 'Paper', 'Scissor')
count=0
plr_1=''
plr_2=''
while count < 3:
    print(count)
    plr_1=base_choice[randint(0,2)]
    plr_2=base_choice[randint(0,2)]
    if plr_1 == plr_2:
        print(f"plr_1 is {plr_1} and plr_2 is {plr_2} same choice. Continuing")
    #Player 1 is rock, player 2 could be scissors or paper
    elif plr_1 == 'Rocks':
        if plr_2 == 'Scissor':
            print(f"plr 1 is {plr_1} and plr_2 is {plr_2}. plr_1 wins")
        elif plr_2 == 'Paper':
            print(f"plr 1 is {plr_1} and plr_2 is {plr_2}. plr_2 wins")
    #Player 1 is Paper
    elif plr_1 == 'Paper':
        if plr_2 == 'Scissor':
            print(f"plr 1 is {plr_1} and plr_2 is {plr_2}. plr_2 wins")
        elif plr_2 == 'Rock':
            print(f"plr 1 is {plr_1} and plr_2 is {plr_2}. plr_1 wins")
    # Player 1 is Scissor
    elif plr_1 == 'Scissor':
        if plr_2 == 'Paper':
            print(f"plr 1 is {plr_1} and plr_2 is {plr_2}. plr_1 wins")
        elif plr_2 == 'Rock':
            print(f"plr 1 is {plr_1} and plr_2 is {plr_2}. plr_2 wins")
    else:
        if count == 2:
            print("Sorry!no. of tries over")

    count += 1


