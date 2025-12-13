# Create a game to play guessing of numbers

# Define a range for guessing
# You need to ask for guessed number
# conditional check to validate the guess
# Add re-attempting

from random import randint

number = randint(1,50)
print("Guessed No. is, ", number)
count = 0
user_guess = int(input("Enter your guessed number between 1 - 50: "))
while user_guess != number: #Start looping until user guesses right or for 5 guesses
    #print("Try again")
    #if count > 0 and count < 5:
        #user_guess = int(input("Enter your guessed number between 1 - 50: "))
    if abs(user_guess - number) > 10 :
       user_guess = int(input("Guessed to high. Guess again and enter: "))
    elif abs(user_guess - number) < 10 and abs(user_guess - number) > 4:
       user_guess = int(input("Moderately closer guess. Guess again and enter: "))
    elif abs(user_guess - number) < 4:
       user_guess = int(input("Moderately closer guess. Guess again and enter: "))
    # elif count > 4:
    #     print("no if guesses is only 5 and over. Exiting...") #Limit no of guesses
    #     break
    count +=1 # Increment count of loop variable

#if count >= 4:
if  user_guess == number:
    print("congratulations!!! You have guessed right!!!")
