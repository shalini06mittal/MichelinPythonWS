
'''
1. 2 files will be created: 
category.txt[ that stores list of all categories]
words.txt [ that stores words for respective category]
ex: 
sports: cricket,badminton,football,basketball,hockey
flowers: roses,lotus,jasmine,sunflower,mogra
cities: mumbai,delhi,pune,patna,panji
'''

import random

words=[]

def addCategoy(category):
    '''
        add the category in the category.txt file
    '''
    pass
def addwords(count, category):
    '''
        for the count take words as input and add in words list
        do not forget to use global to access list
        create a loop and take all words as input 
        and store the words list in the file words.txt
    '''
    pass

def jumbledwords(word):
    '''
        shuffle the word return the  jumbled word
    '''
    pass

def readwords(category):
    '''
    will read all the word fron the words.txt and store in the words=[]
    '''
    pass
    
def getCategories():
    # read all categories from file category.txt and return the list
    pass

def startgame():
   '''
    display a jumbled word and ask the user to guess the correct word
    give user 3 tries to guess.
   '''
   while True:
        print('CHoose any 1 of the options')
        print('1. Add words')
        print('2. Play Game' )
        print('3. Exit' )
        choice = int(input('Choose'))
        if choice == 1:
            category = input('enter category')
            #add the category in the file category.txt
            noofwords = int(input('how many words'))
            addwords(noofwords, category)
        elif choice == 2:
            # get list of catefories from the category.txt file
            categories = getCategories()
            print(categories)
            for index in range(len(categories)):
                print(index+1,categories[index])
            catchoice = int(input('Choose category to play: '))
            # print(catchoice)
            readwords(categories[catchoice-1])
            # print(words)
            pos = random.randrange(0, len(words))
            correctans = words[pos]
            wordtoguess = jumbledwords(correctans)
            print(wordtoguess)
            userguess = input('Guess the right word?')
            if userguess == correctans:
                print('YEAHH')
            else:
                print('Better luck next time')
        else:
            print('Thanks')
            break
   


startgame()



