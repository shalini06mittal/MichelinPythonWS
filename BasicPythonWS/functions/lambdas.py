'''
lambdas are a concise way of writing the implementation of a function
small, anonymous function that can take any number of arguments but only have 1 expression
lambdas return an object or the reference to the function definition that can be called at a later stage
lambda functions are restricted to s single expression and no need of return keyword it is implicitly evaluated

syntax:
lambda arguments : body/ expression
'''
def squares(no):
    return no*no

sq = lambda no : no*no

print(sq(10))

names = ['Shalini Mittal','Ajay Gupta','Manas Sharma','Joe Austin','Ria Sana']

# # bubble sort
# for i in range(len(names)-1):
#     for j in range(len(names)-1):
#         print(names[j])
#         if len(names[j]) > len(names[j+1]):
#             temp = names[j]
#             names[j] = names[j+1]
#             names[j+1] = temp
        

# # print(names)
# # def splitnames(name):
# #     print(name)
# #     return name.split()[1]

# def length(name):
#     c = 0
#     for v in name: 
#         c+=1
#     return c

# def outer(x):
#     def inner(y):
#         return x+y
    
# x = lambda x: lambda y : x+y

names.sort(key=lambda name:name.split()[1] )
# print(names)
# names.sort(key=length )
# print(names)

# '''
# create a list of 2-digit numbers and sort the list on the basis of last digit
# 23 89 45 76 32
# 32 23 45 76 89
# '''

# # def lastDigit(no):
# #     return no%10

# list_1 = [12,34,56,16,45,78,95,56]

# list_1.sort(key = lambda no: no%10)

# # print(list_1)


# players = [('p1',90),('p2',89),('p3',93),('p4',80),('p5',70),('p6',50)]
# # sort on scores of every player
# players.sort(key = lambda player : player[1])
# print(players)