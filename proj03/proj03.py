# Name:
# Date:


""" 
proj 03: Guessing Game

Generate a random number between 1 and 9 (including 1 and 9). 
Ask the user to guess the number, then tell them whether they guessed too low, too high, 
or exactly right. Keep the game going until the user types exit.
Keep track of how many guesses the user has taken, and when the game ends, print this out.

"""
loop_var = True
while loop_var == True:
    counter = 0
    a = raw_input("Enter a number one through fifteen. ")
    a = int(a)
    counter = counter + 1
    import random
    random_num = random.randint(1,15)
    while random_num != a and counter < 5:
        if random_num < a:
            print ('That number is too high. ')
            a = raw_input('Guess again. ')
            a = int(a)
            counter = counter + 1
        if random_num > a:
            print('That number is too low. ')
            a = raw_input('guess again ')
            a = int(a)
            counter = counter + 1
        if random_num == a:
            print ('You guessed the number! ')
            print ('You ran out of guesses!')
            b = raw_input('Would you like to play again? Type yes or no. ')
            b = str(b)
            if b == 'no':
                loop_var = False
        if counter == 5:
            print ('You ran out of guesses!')
            b= raw_input ('Would you like to play again? Type yes or no. ')
            b=str(b)
            if b == 'no':
                loop_var = False