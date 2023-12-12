# looping constructs
'''
for
while
start -> inclusive, stop -˘ exclusive
start = 1, stop = 11, step = 1
start = 1, stop = 11, step = 2 => start + step
1 3 5 7 9
'''
# range => range of values
# start < stop
# default step = 1
# default start = 0
# start = 1, stop = 11, step = 1
# print(list(range(1, 11)))
# print(list(range(1, 12, 2)))
# # start > stop, and step +ve, it returns an empty list
# print(list(range(10, 1)))
# # start > stop, step should be -ve
# print(list(range(10, 1,-1)))

print(range(10))
print(list(range(11)))


# for - in
# v- loop control variable
for v in range(10,21):
    #print(1)
    print(v, v*v)

# strings are iterable sequence
# no of vowels in a string
# c = 0
# for n in 'shalini mittal':
#     if n == 'a' or n == 'e' or n == 'i' or n == 'o' or n == 'u': 
#         print(n)
#         c+=1 # c = c+1
#     print('not in if')
# print(c)
