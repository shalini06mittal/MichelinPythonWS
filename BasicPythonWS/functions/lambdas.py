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

# print(sq(10))

names = ['Shalini Mittal','Ajay Gupta','Manas Sharma','Joe Austin']

print(names)
# def splitnames(name):
#     print(name)
#     return name.split()[1]

names.sort(key=lambda name:name.split()[1] )
print(names)

'''
create a list of 2-digit numbers and sort the list on the basis of last digit
23 89 45 76 32
32 23 45 76 89
'''
