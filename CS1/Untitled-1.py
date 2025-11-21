import random

number = 2 
guesses = 5

while guesses > 0:
    guess = int(input('2:'))

    if guesses > 2:
        print(f'too high! you have {guesses-1} left')
    elif guess < '2':
        print('too low')
    else:
        print('you got it!')
        break 
    guesses -= 1


