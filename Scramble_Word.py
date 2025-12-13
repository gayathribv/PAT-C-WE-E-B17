# From a list of words choose and scramble and display
# If user guesses correctly then ask for input switch to next scrambled word
import random
Lst_str=["python", "javascript", "automation", "pytest", "guvi", "selenium"]
Loop_var=0
while Loop_var <= 5:
    Scrambled_Word=list(Lst_str[Loop_var])
    random.shuffle(Scrambled_Word)
    Scrambled_Word=''.join(Scrambled_Word)
    print(Scrambled_Word)
    User_guess = input("Enter Your Guess: ")
    if User_guess != Lst_str[Loop_var]:
        print("Good guess. But Try again")
        continue
    elif User_guess == Lst_str[Loop_var]:
        Usr_choice=input("Wow. What a match!!Do you want to continue Guessing Y/N: ")
        if Usr_choice == 'Y' or Usr_choice == 'y':
            Loop_var +=1
            continue
        else:
            break


