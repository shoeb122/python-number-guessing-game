import random

print("Welcome to the  Game!, this is a number guessing game /n you got 5 attempts to guess the number between 50 and 100, lets start the Game")

number_to_guess =random.randrange(50,100)

chances = 5
guess_counter = 0

while guess_counter < chances:
    guess_counter += 1
    my_guess = int(input(
        "Enter your guess:" ))
    if my_guess == number_to_guess:
        print(f"the number is {number_to_guess} and you guessd it right in {guess_counter}attempts")
    elif guess_counter >=chances and my_guess != number_to_guess:
        print(f"oops sorry, the number is {number_to_guess} better luck next time")
    elif my_guess < number_to_guess:
       print("your guess is too low, try again")
    elif my_guess > number_to_guess:
        print("your guess is too high, try again")   
        
   
    
    
    
    
    
    
    
    
    
    
    


