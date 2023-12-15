'''
immutable
indexing
https://realpython.com/python-and-operator/
'''
# \t -> tab key
# sent = 'technology trends\nhello'
# sent = 'technology \ttrends'
# print(sent)
# # len() -> gives the number of characters
# print(len(sent))
# # indexing
# print(sent[0])
# print(sent[16])
# print(sent[9])
# print(sent)
# print('**'+sent[11]+'**')
# print(sent[11])

# length = len(sent)

# print(sent[length-1])

# print(length)
# print((len(sent))-1)
 
# # loops to access every character
# for ch in sent:
#     print(ch)

# length = len(sent) #18
# for index in range(length):
#     print(index, sent[index])


# functions -> general functions available for most of the data types and data structure

color = 'lightgreen'

print(len(color))
print(max(color))
print(min(color))
print(sorted(color))
print(color)

# methods -> accessed on the data structure, they are sepcific to the type of data
print(color.upper())
print(color.lower())
print(color.capitalize())
print(color.endswith('green'))
print(color.startswith('light'))
print(color.index('green'))
# print(color.join(' is a soft color'))
text = '     some     text     '
print('*'+text+'*')
print('*'+text.lstrip()+'*')
print('*'+text.rstrip()+'*')
print('*'+text.strip()+'*')
text = 'where there is will there is way'
print(text.split())
data ='shalini, 12312213,89,mumbai, india'
print(data.split('i'))
# color[0] = 'br' ->immutable

print('123123'.isalnum())
print('123123'.isalpha())
print('123123'.isdecimal())
print('123123'.isdigit())
print('123123'.isspace())
print()
print('1231jahs23'.isalnum())
print('jahdas asdasd'.isalpha())
print('decimal','123123.67'.isdecimal())
print('123123'.isdigit())
print('  '.isspace())

print('shalini'=='shalini')
print('shalini'==' shalini')
print(''.isspace())

# '' '  ' None
name = None
c = None
print(name ==c)
if name:
    print(1)
else:
    print(2)

# operators in string
print('\n========== OPERATORS ==============\n')
print('Ms. '+'Shalini')
# print('@'+2)# error
print('@'*2)
# print('@'*'2')

#in -> membership operator
print('_' in 'shalini_mittal')
print('red' in 'rose is red and sky is blue')
# not in
print('_' not in 'shalini@mittal')
print('red' not in 'rose is red and sky is blue')

print(1 and 3)
print(1 and None)
print(None and 1)
print(1 or '')
print('' or 5)

no = None
if no:
    print('hey')
else:
    print('bye')

'''
Take a sentence as input from the user and print the longest word

'''
words =['hello','welcome','beautiful','lovelines','zebra']
sortedwords = sorted(words, key=len, reverse=True)
print(sortedwords)
print(sortedwords[0])
length = len(sortedwords[0])
print('*****************')
for word in sortedwords:
    if len(word) != length:
        break
    print(word)
# words =['asha','apples','ack','aura','anxiety']
# words=['hello','my','family']
words = 'hello world how are you'.split()
print(max(words)) # defalt max searches on the asii value
print(max(words, key=len))# basis or parameter on which to find the max