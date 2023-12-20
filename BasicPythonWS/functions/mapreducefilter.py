nos = [14,42,63,42,59]
# nos1 = []
# for n in nos:
#     d = n%10 * 2
#     nos1.append(d)

# print(nos1)

def transform(n):
    d = n%10 * 2
    return d
t = list(map(transform, nos))
# print(map(lambda n : n%10 * 2, nos))
# print(t)

'''
take a list of random 5 url that start with http
transform every http to https and return it as a new list
'''
urls=['http://www.ex1.com','http://www.ex2.com','http://www.ex3.com','http://www.ex4.com','http://www.ex5.com']
# print(list(map(lambda url : url.replace('http', 'https'), urls)))

def change(one, *two):
 	print(type(two))
# change(1,2,3,4)

# filter => filtering out values

marks = [23,35,78,90,99,12,5,45]
def filterMarks(m):
      print('m',m)
      if m >=50:
            return m

# print(list(filter(filterMarks, marks)))
# print(list(filter(lambda m : m>=50, marks)))

#reduce
from functools import reduce

amount = [12,34,2,5,6]

def getSum(x,y):
      print(x, y)
      return str(x)+' '+str(y)
res = reduce(getSum, amount,100)
res = reduce(lambda x,y: x+y, amount,100)
print(res)
# s = 0
# for amt in amount:
#       s+=amt
# print(s)

# s = amount[0]
# for i in range(1, len(amount)):
#       s+=amount[i]
# print(s)

# s = amount[0]
# for amt in amount:
#       if amt == amount[0]: continue
#       s+=amt
# print(s)

'''
1. Create a list as follows with every word from the sentence, use map
Ex: 'Python lambdas are cool'
Output:
['PYTHON','python',6]
['LAMBDAS','lambdas',7]
['ARE','are',3]
['COOL','cool',4]
'''
sentence = 'Python lambdas are cool'
res = map(lambda word: [word.upper(), word.lower(), len(word)], sentence.split())
# print(list(res))
for r in res:
      print(r)
'''
2. find the values common in 2 lists using filter
l1 = [1,2,3,4,5,6,7]
l2=[2,3,5,6,8,9]
output: [2,3,5,6]
'''
l1 = [1,2,3,4,5,6,7]
l2=[2,3,5,6,8,9]
print(list(filter(lambda v1: v1 in l2, l1)))


