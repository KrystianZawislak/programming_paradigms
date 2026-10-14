import random
random_int = random.randint(1, 10)
user_guesses = 0
guess = int(input("Guess the number: "))

while (random_int != guess):
    if (user_guesses == 2):
        print("End of trial")
        break
    if (guess > random_int):
        print("Lower")
    elif (guess < random_int):
        print("Higer")
    user_guesses += 1
    guess = int(input("Guess the number: "))
else:
    print("You guessed right!")
