import time

print('Alarm!')                                                   #display: Alarm!

while True:                                                       #forever loop
    while True:                                                   #forever loop
        snooze = input('Snooze? Yes or no?')                      #prompt user for response to snooze, convert to lowercase, and store in variable 


        if snooze == 'no':                                        #if user input = no, do this
            print('Wake up and get out of bed.')                  #display message
            break                                                 #end forever loop
        else:                                                     #if user responds anything else
            print('Go back to sleep for 5 minutes.')              #display message
            time.sleep(2)                                         #pause program for 2 seconds

    hunger = input ('Are you hungry?')                            #prompt user for response to eat, convert to lowercase, and store in variable

    if hunger == 'yes':                                           #if user input = yes, do this
        print('Eat breakfast')                                    #display message
        time.sleep(2)                                             #pause program for 2 seconds 
        print('Go to the bathroom')                               #display message
    else:                                                         #if user responds anything else
        print('Go to the bathroom.')                              #display message
    
    while True:                                                   #forever loop
        hair = input ('Do you like your hair today?')             #prompt user for response for hair, convert to lowercase, and store in variable 
              

        if hair == 'yes':                                         #if user input = yes, do this    
            print('Go to your room to get dresssed.')             #display message
            break                                                 #end forever loop
        else:                                                     #if user reponds anything else
            print('Fix it!')                                      #display message
            time.sleep(2)                                         #pause program for 2 seconds

    while True:                                                   #forever loop
        shirt = input('Do you want to wear your red shirt?')      #prompt user for response for shirt, convert to lowercase, and store in variable 
       
        if shirt == 'yes':                                        #if user input = yes, do this
            print('Put on red shirt')                             #display message
            break                                                 #end forever loop
        else:                                                     #if user responds anything else
            print('Check what other shirts you have.')            #display message
            time.sleep(2)                                         #pause program for 2 seconds
    print('Grab your backpack and get into your car.')            #display message

    while True:                                                   #forever loop  
        temp = input ('Are you too cold in your car?')            #prompt user for response for temp, convert to lowercase, and store in variable 

        if temp =='no':                                           #if user input = no, do this
            print ('Turn the AC on.')                             #display message
            break                                                 #end forever loop
        else:                                                     #if user responds anything else
            print('Turn the heat up!')                            #display message
            time.sleep(2)                                         #pause program for 2 seconds
    print('Start driving!')                                       #display message

    music = input('Do you listen to music during the ride?')     #prompt user for response for music, convert to lowercase, and store in variable 

    if music =='yes':                                            #if user input = yes, do this
        print('Get airpods out of bag and put them in.')         #display message
        time.sleep(2)                                            #pause program for 2 seconds
    else:                                                        #if user responds anything else
        print('Look out the window and enjoy the ride!')         #diplay message 
        time.sleep(2)                                            #pause program for 2 seconds
    print('You have arrived at school, have a good day!')        #display message
