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
print(map(lambda n : n%10 * 2, nos))
print(t)

'''
take a list of random 5 url that start with http
transform every http to https and return it as a new list
'''
urls=['http://www.ex1.com','http://www.ex2.com','http://www.ex3.com','http://www.ex4.com','http://www.ex5.com']
print(list(map(lambda url : url.replace('http', 'https'), urls)))



