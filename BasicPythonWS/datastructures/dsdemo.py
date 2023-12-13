'''
x1 = 10
x2
x3
x4
loc1_dec = 324234,234234,8789,9867986,....
data structures -> to store more than 1 data/value in a variable/containers

immutable(cannot change) and mutable(can change)

indexing => allows to access data stored at a particular location

string -> combination or more than 1 character [alphabets, numbers and symbols]
supports indexing
'shalin_i123@gmail.com' ""

tuple, list and set store comma separated values
tuple -> immutable ( once a structure is created it cannot be altered , not even the value-> which 10 items )
duplicates are allowed, indexing [ 0 ]
constant, ex: to store vowels, month names, days of the week
10 20 shalini India red 987 213
() or ,

list -> mutable (can modify the size as well as the data)
duplicates are allowed, indexing [ 0 ]
10 20 ajay India red 987 213
[]

set ->  mutable (can modify the size as well as the data)
duplicates are not allowed, no indexing
10 20 ajay India red 987 213
{}

dictionary -> mutable (can modify the size as well as the data)
key-value pairs format, where every key:value is separated by a : and key-value pair by a ,
keys cannot be duplicate but value can be
indexing is not supprted , keys to access the data
phone = 5676543526
accno = 8939291019

city: 'Singapore'
country:'Singapore'

{}
'''

name = 'shalini'
t1 = (1,2,3,'a')
l1 = [1,2,3,4,3.4, 'red']
s1 = {1,2}
d1 = {'city':'Mumbai', 'country':'India', 2:8678987}

print(type(name))
print(type(t1))
print(type(l1))
print(type(s1))
print(type(d1))