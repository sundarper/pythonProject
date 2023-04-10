import random

low = 1
high = 1000
computerGuess = random.randint(low, high)
print("Computer guess : ", computerGuess)

while True:
    userGuess = int(input(f"Guess the number which Computer has generated between {low}, {high}: "))
    if computerGuess == userGuess:
        print("Matches")
        break
    elif userGuess < computerGuess:
        low = userGuess
    else:
        high = userGuess


