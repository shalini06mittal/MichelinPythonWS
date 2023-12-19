# nested function in python

def m1():
    print('1 in m1')
    def m2():
        print('2 in m2')
    m2 = 10
    return m2

# print(m1())
'''
1 in m1
2 in m2
'''
# m1()()
ref = m1()
# print(ref)
# ref()


# def f1():
#     print('f1')
# print(f1())

# count = 0
# closures, lexical scoping of the variable
def counter():
    count = 0
    def incr():
        nonlocal count
        count+=1
    def decr():
        nonlocal count
        count-=1
    def getCount():
        return count
    return {'incr':incr, 'decr':decr, 'count':getCount}

c = counter()
# print(c)
c['incr']()
c['incr']()
c['incr']()
c['incr']()
print(c['count']())
c['decr']()
print(c['count']())

