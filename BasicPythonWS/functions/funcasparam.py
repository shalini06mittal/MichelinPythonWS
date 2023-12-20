def squares(no):
    return no*no

s = squares
print(s(10))
'''
func is a refernce to a function that can be called from within the calculate()?
to the implementation of the function
'''
def calculate(nos, func:function|None):# nos=[1,2,3,4,5], func = squares
    print(type(func))
    for n in nos:
        print(func(n))

def cube(no):
    return no*no*no

calculate([1,2,3,4,5], lambda x:x*x)
calculate([1,2,3,4,5], cube)