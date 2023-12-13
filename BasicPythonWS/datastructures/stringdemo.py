'''
immutable
indexing
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
# color[0] = 'br' ->immutable