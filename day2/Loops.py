number = int(input('enter a number'))
i = 1
while i < 11:
    print(number * i)
    i += 1
# while loop with else
x = 1
while x < 3:
    print(x)
    x += 1
else:
    print('limit crossed')
# Guessing game
# Generate a random integer between 1 and 100
import random

jackpot = random.randint(1, 100)
guess = int(input('Guess the number'))
counter = 1
while guess != jackpot:
    if guess < jackpot:
        print('wrong! guess higher')
    else:
        print('wrong! guess lower')
    guess = int(input('Guess the number once again'))
    counter += 1
else:
    print('Correct guess')
    print('attempts', counter)
