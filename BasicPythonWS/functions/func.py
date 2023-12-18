import random
'''
roll 2 dices
min - 2
max - 12
user had to choose either one of the option
7 up 7 down?
1. <7
2. >7
3. ==7
'''
# function -> verbs => doing something
# defined a function whose name is winMessage and it has a job to do
# job is defined after the :
# FUNCTIONS ARE reusable components, modularity
def winMessage():
    print('YOU HAVE WON, PLEASE COLLECT YOUR AMOUNT FROM THE COUNTER!!')
    # variables, if-else, loops , call other functions, define nested functions
   
def looseMessage():
    print('You LOOSE!!!')

def randomNumber():
    return random.randrange(1, 7)

choice = int(input('Choose : \n1. Less than 7\n2. Greater than 7\n3. Equal to 7'))
dice1 = randomNumber()
dice2 = randomNumber()
s = dice1 + dice2
print('Dice roll',s)
if choice == 1 and s < 7:
   winMessage()
elif choice == 2 and s>7:
    winMessage()
elif choice == 3 and s==7:
    winMessage()
else:
    print('YOU LOOSE - THE VALUE WAS', s, ' and you chose', choice)
