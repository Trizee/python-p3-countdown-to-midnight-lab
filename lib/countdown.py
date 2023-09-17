# your code goes here!
import time

def countdown(number = 10):

    while number > 0:
        print(f'{number} SECOND(S)!')
        number -= 1
    
    print('HAPPY NEW YEAR!')

countdown()

def countdown_with_sleep(number):

    while number:
        print(f'{number} SECOND(S)!')
        number -= 1
        time.sleep(1)

    print('HAPPY NEW YEAR!')

countdown_with_sleep(10)