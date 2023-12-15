# slicing -> get a slice from something
string = 'motivation'

# python supports -ve index. starts from -1 to -len

# print(string[0])
# print(string[-1])

# # slicing -> start=0, stop, step=1
# # [start:stop:step]
# print(string[0:5])
# print(string[:5])
# # len
# print(string[5:])

print(string[::1])
print(string[-1::1])
print(string[-1::-1])

print(string[::-1]) # step = -1 start = -1. stop = -11
print(string[:5:-1]) # 
print(string[:-5:-1]) # 
print(string[9:2:-2])
print(string[-6:6])

# print(string[slice(5)])
print()
text = 'hey'
while text:
    print(text)
    text = text[1:]
print('text',text)
