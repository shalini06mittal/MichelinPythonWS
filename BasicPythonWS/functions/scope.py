# local scope and global scope
# print(x)
# # 1
# x = 10
# def m1():
#     print('1',x) # 10

# print('2',x) # 10
# m1()

# # 2
# x = 10
# def m1():
#     x = 20
#     print('1',x) # 20

# print('2',x) # 10
# m1()
# print('3',x) # 10

# # 3
# x = 10 # global in the module => scope.py
# def m1():
#     #global variables are read only inside a function
#     x = 20 # local variable in the function with name same as global variable
#     print('1',x) # 20

# print('2',x) # 10
# m1()
# x = 100
# print('3',x) # 100

# # 4
# x = 10 # global in the module => scope.py
# def m1():
#     #global variables are read only inside a function
#     # to make it read and write refer it using global keyword
#     global x # whenever x is being referred in the function it is pointing to global x
#     x = 20 # here the changes are made to the global instance only
#     print('1',x) # 20

# print('2',x) # 10
# m1()
# print('4',x) # 20
# x = 100
# print('3',x) # 100

# 5
x = 10 # global in the module => scope.py
# hoisting in javascript
def m1():
    #global variables are read only inside a function
    # to make it read and write refer it using global keyword
    #cannot access local variable 'x' where it is not associated with a value
    #print('5',x) # name 'x' is used prior to global declaration
    global x # whenever x is being referred in the function it is pointing to global x
    x = 20 # here the changes are made to the global instance only
    print('1',x) # 20

print('2',x) # 10
m1()
print('4',x) # 20
x = 100
print('3',x) # 100

l=[]
def m1():
    l.append(10)
    print(l)
print(l)
m1()
print(l)