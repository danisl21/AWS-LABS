
import random
print("welcome to Guess the Number!")
print("The rules are simple. I will think of a number, and you will try to guess it")
number = random.randint(1,10)
isGuessright= False

while isGuessright != True:
    guess = input("Guess a number between 1 and 10: ")
    if int(guess) == number:
        print("you guessed {}. That is correct! You win!" .format(guess))
        isGuessright == True

    else:
        print("you guessed {}. Sorry, that isn't it. Try again" .format(guess))
