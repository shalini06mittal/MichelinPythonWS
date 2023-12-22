import random
import os
'''
1. create a table in database as follows:

tablename : words
columns : id int PK, word, jumbled

'''

from mysql import connector as con;

#mamp
dbcon = con.connect(host='localhost',
                    user='root',
                    passwd='root',
                    port=8889,
                    database='techgatha')
words=[]
# cricket, football, basketball
# ricckte, 

def addwords(count, category):
    '''
        for the count take words as input and add in words list
        do not forget to use global to access list
        create a loop and take a word as input and jumble it calling jumbledwords()
        and store the
        word and jumble word in database
        insert
    '''
    for i in range(count):
        word = input('enter a word') # cricket
        # insert a record in database
        query = 'insert into words(word, category) values(%s,%s)' 
        cursor = dbcon.cursor()
        cursor.execute(query, (word, category))
        dbcon.commit()
    pass
def jumbledwords(word):
    '''
        shuffle the word return the  jumbled word
    '''
    newword = list(word) # cricket , newword ['c','r','i','c','k','e','t']
    # print(newword)
    random.shuffle(newword)
    jumble = ''.join(newword)
    return jumble

def readwords(category):
    '''
    will read all the word and jubmled words from the database and store
    in words and jumbled respectively
    '''
    # print('read',category)
    query = 'select word from words where category=%s' 
    #query = "select word, jumbled from words where category='"+category+"'"
    cursor = dbcon.cursor()
    cursor.execute(query,(category,))
    data = cursor.fetchall()
    # print(data)
    global words
    for item in data:
        words.append(item[0])
    
        

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
            noofwords = int(input('how many words'))
            addwords(noofwords, category)
        elif choice == 2:
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
                print('Better luck next time: right word was ', correctans)
        else:
            print('Thanks')
            break
   
def getCategories():
    query = 'select distinct(category) from words' 
    cursor = dbcon.cursor()
    cursor.execute(query)
    categorylist = cursor.fetchall()
    categories = []
    for category in categorylist:
        categories.append(category[0])
    return categories

startgame()



