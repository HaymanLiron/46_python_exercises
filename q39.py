import random

# guess the number game
# number is between 1 and 20
MIN_NUM = 1
MAX_NUM = 20

secret_number = random.randint(MIN_NUM, MAX_NUM + 1)
guessed = False

name = input("What is your name?")
print("Well, " + name + ", I am thinking of a number between 1 and 20.")

while not guessed:
    valid_guess = False
    while not valid_guess:
        guess = input("Take a guess.")
        try:
            guess = int(guess)
            if guess in range(MIN_NUM, MAX_NUM + 1):
                valid_guess = True
            else:
                print("Number out of range!")
        except:
            print("Invalid guess!")
    if guess < secret_number:
        print("Your guess is too low!")
    elif guess > secret_number:
        print("Your guess is too high!")
    else:
        guessed = True
        print("Congratulations " + name + "! You guessed it!")

