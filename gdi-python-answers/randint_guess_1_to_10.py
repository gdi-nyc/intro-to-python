from random import randint

def random_number():
    secret_number = randint(1, 10)
    guess = raw_input("Guess the secret number between 1 and 10")
    guess = int(guess)

    if guess < 1 or guess > 10:
        print "That's not a guess between 1 and 10!"
    elif guess > secret_number:
        print "That's too high"
    elif guess < secret_number:
        print "That's too low"
    else:
        print "You got it right!"

random_number()
