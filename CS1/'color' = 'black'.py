color = 'black'
guess = input('enter your color guess; ')
while True:
    if color == guess:
        print('you got it!')
        break 
    else:
        print('try again!')