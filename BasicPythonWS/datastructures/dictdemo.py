# d1 = {}
# d1 = dict()
d1 ={"eid":1, 'ename':'Shalini','city':'Mumbai','phonenos':[123123,234234]}
print(type(d1))
print(d1)
print(len(d1))
# access values
print(d1.get('eid'))
print(d1['phonenos'])
print()
for n in d1:
    print(n, d1[n])
print()
d1['ename'] = 'SHalini MIttal'
print(d1)
d1['country'] ='India'
print(d1)
d1.update({'city':'Pune'})
print(d1)
print(d1.keys())
print(d1.items())
print(d1.pop('country'))
print(d1)

for values in d1.values():
    print(values)

for k,v in d1.items():
    print(k,v)
    v='hello'
    print(v)

print()
for d in d1.items():
    print(type(d))
    print(d[0], d[1])

players = ('p1','p2','p3')
#{p1:0, p2:0, p3:0}
leaderboard = dict.fromkeys(players, 0)
print(leaderboard)

'''
consider you have a list of people
people = ['abc','xyz','abc','d','f','d','d','e']
Create a dictionary by key as the name and value os the count for the name
{'abc':2, 'xyz':1,'d':3,'f':1,'e':1}
'''
d1 = {(1,2):'One','Two':2}
print(d1)


