
'''
jumbled words
['red','blue]
['der','ebul']
1. category -> colors
10 words as input from the user => list, words
jumbledwords = every word from the list jumbled and stored in this DS

1. Create 2 empty list => words, jumbledwords
2. Create a function input that takes parameter for the category and asks the user
to enter 10 words in that category and put them in the empty set create in step 1
3. Create a function jumble that jumbles every word from the set stored in jumbledwords set

4. Create a function startPlay() that asks the user if they ok to begin then display
a random word from the jumbledwords and ask the user to guess the word
then display the message correct or wrong, If wrong also display the right answer
then call the startplay() function
'''

import random
# global variables 
words= []
jumblewords= []
# ['red','blue','green','yellow','black','pink','brown','white','violet','orange']
# ['der', 'ulbe', 'ngere', 'eolwyl', 'blakc', 'npik', 'rbnow', 'htwie', 'teoliv', 'aerong']
def inputWords(category):
    print('Category', category)
    #global words
    words.extend(eval(input('enter 10 words as list\n')))
    for word in words:
        jumblewords.append(jumbledWords(word))

def jumbledWords(word):
    '''
        shuffle the word return the  jumbled word
    '''
    newword = list(word) 
    random.shuffle(newword)
    jumble = ''.join(newword)
    return jumble


# print(random.sample(['red','blue','green','yellow','black','pink','brown','white','violet','orange'], 10))
# print(random.sample('red', 3))
inputWords('Colors')
jumbledWords()
print(words)
print(jumblewords)

# import random
# words = []
# jumbled_words = []
# def user_input(category):
#     for _ in range(5):
#         word = input(f"Enter a {category} word: ")
#         words.append(word)
#     print(words)

# def jumble():
#     for word in words:
#         jumbled_word = list(word)
#         random.shuffle(jumbled_word)
#         jumbled_words.append(''.join(jumbled_word))
#     print(jumbled_words)
 
# def start_play():
#     ready = input("Are you ready to begin? (yes/no): ")
#     if ready.lower() == 'yes':
#         random_index = random.randint(0, 4)
#         selected_word = jumbled_words[random_index]
#         user_guess = input(f"Guess the word: {selected_word}\nYour guess: ")
#         if user_guess.lower() == words[random_index].lower():
#             print("Correct!")
#         else:
#             print(f"Wrong! The correct word is: {words[random_index]}")
#         play_again = input("Do you want to play again? (yes/no): ")
#         if play_again.lower() == 'yes':
#             start_play()
#         else:
#             print("Thanks for playing!")

 
# user_input("colors")
# jumble()
# start_play()

