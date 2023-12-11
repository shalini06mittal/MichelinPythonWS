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
# print(list(range(11)))
# for - in
# for v in range(1,11):
#     print(1)
# strings are iterable sequence
# no of vowels in a string
# c = 0
# for n in 'shalini mittal':
#     if n == 'a' or n == 'e' or n == 'i' or n == 'o' or n == 'u': 
#         print(n)
#         c+=1 # c = c+1
#     print('not in if')
# print(c)

# while
'''
start value
while <conditional expression>:
    statements to execute till the condition is true
    update start
'''
# start = 1 # loop control variable
# while start <= 5: # start = 1
#     print(start)
#     start = start+1

# print sqaures of 5 random numbers taken an input from the user       
# when number of iterations are fixed
# for i in range(5): # 0 1 2 3 4
#     no = int(input('enter a no'))
#     print(no * no)

# when number of iterations not fixed
# s =1 
# while s<=5:
#     no = int(input('enter a no'))
#     print(no * no)
#     s+=1
# print sqaures of random numbers taken as input from the user  ,
# until user quits => 0

stop = -1
while stop != 0:
    no = int(input('enter a no'))
    print(no * no)
    stop = int(input('enter 0 to stop or any value to continue'))
    if stop == 0:
        print('Thanks')