# arbitrary arguments
# def calculate(a = []):
#     squares =[]
#     for i in a:
#         squares.append(i*i)
#     return squares

def calculate(*args, power=2):
    print(args)
    squares =[]
    for i in args:
        squares.append(i**power)
    return squares

# print(calculate(1,2,3,4,5, power= 3))
# print(calculate(1,2,3,4,5))

# keyword arguments
def display(x, *args, **kwargs):
    # print(kwargs)
    # print(args)
    # print(x)
    for k,v in kwargs.items():
        print(k,v)
display(1,2,3,4,5,name='shalini', city='Mumbai')

d1 = {'name':'Mr.X', 'email':'x@g.com'}
for d, v in d1.items():
    print(d, v)    

from func import looseMessage
looseMessage()