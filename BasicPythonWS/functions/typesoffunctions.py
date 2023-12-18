
'''
1. def keyword
2. name of the function followed by () and a :
3. input if it takes any then it has to be passed via parameters in the () of the function name
4. body of the functioni.e business logic , the block of statements to be executed whe this function
is called
5. output if any by using the return keyword
'''
# 1. function with no parameters and no returnn type
import time
# print(time.strftime("%p"))
def greet():
    now = time.strftime("%p")
    if now == 'AM':
        print('GOOD MORNING')
    else:
        print('GOOD EVENING')

    
# print(greet())
# print()
# 2. function with no parameters but has a returnn typedef greet():
# function should just do the calculation and leave the rest of how to print to the caller
# reusable function
'''
return keyword to return the output. The moment a return keyword is executed the control 
immediately transfers back to the caller
there can be multiple return keywords but they have to be conditional
'''

def greetWithReturn():
    # print('greet with return called')
    now = time.strftime("%p")
    if now == 'AM':
        return
    else:
        return 'GOOD EVENING'
    
message = greetWithReturn()
# print(message)
# print(greetWithReturn())

'''
Create a function calculate that takes 2 numbers from the user and returns the 
addition of those 2 numbers
'''

# 3. function can take input but return nothing
# required positional argument: 'name'
def greetWithInput(fname, lname):
    now = time.strftime("%p")
    if now == 'AM':
        print('GOOD MORNING',fname+' '+lname)
    else:
        print('GOOD EVENING',fname+' '+lname)

greetWithInput('Shalini','Mittal')

# 4. function can take input and also return 
# required positional argument: 'name'
def greetWithInput(fname, lname):
    now = time.strftime("%p")
    if now == 'AM':
        return 'GOOD MORNING '+fname+' '+lname
    else:
        return 'GOOD EVENING '+fname+' '+lname

print(greetWithInput('Richa','Gupta'))

