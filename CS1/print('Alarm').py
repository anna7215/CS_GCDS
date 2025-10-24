import time

print('Alarm!')

while True:
    while True:
        snooze = input('Snooze? Yes or no?')

        if snooze == 'no':
            print('Wake up and get out of bed.')
            break
        else: 
            print('Go back to sleep for 5 minutes.') 
            time.sleep(2)

    hunger = input ('Are you hungry?')

    if hunger == 'yes':
        print('Eat breakfast')
        time.sleep(2)
        print('Go to the bathroom')
    else:
        print('Go to the bathroom.')
    
    while True:
        hair = input ('Do you like your hair today?')

        if hair == 'yes':
            print('Go to your room to get dresssed.')
            break
        else:
            print('Fix it!')    
            time.sleep(2)

    while True:
        shirt = input('Do you want to wear your red shirt?')
       
        if shirt == 'yes':
            print('Put on red shirt')
            break
        else:
            print('Check what other shirts you have.')
            time.sleep(2)
    print('Grab your backpack and get into your car')

    while True:
        temp = input ('Are you too cold in your car?')

        if temp =='no':
            print ('Turn the AC on.')
            break
        else:
            print('Turn the heat up!')
            time.sleep(2)
    print('Start driving!')

    music = input('Do you listen to music during the ride?')

    if music =='yes':
        print('Get airpods out of bag and put them in.')
    else:
        print('Look out the window and enjoy the ride!')
        time.sleep(2)
    print('You have arrived at school, have a good day!')



        

    
   



    

