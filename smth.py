print("=====Welcome to python number guessing game====")
key = 22
print("NNote that you have only 5 chances to guess the correct number.")
chances = 5
while chances > 0:
    guess = int(input("Enter your guess: "))
    if guess < key:
        print("Your guess is too low. Try again.")
    elif guess > key:
        print("Your guess is too high. Try again.")
    else:
        print("Congratulations! You've guessed the correct number.")
        break