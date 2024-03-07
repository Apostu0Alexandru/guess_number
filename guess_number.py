import random

min_value = 1
max_value = 100

secret_number=random.randint(min_value,max_value)

max_guesses = 5

num_guesses = 0
guessed=False

while not guessed and num_guesses < max_guesses:
    try:
        guess=int(input("Guess a number between {} and  {}: ".format(min_value, max_value)))
    except ValueError:
        print ("Enter a valid number")
        continue
    num_guesses+=1

    if guess < secret_number:
        print ("Too low, try again :) ")
    elif guess >secret_number:
        print ("Too big man")
    else :
        print ("Now you have the secret number")
        guessed=True
