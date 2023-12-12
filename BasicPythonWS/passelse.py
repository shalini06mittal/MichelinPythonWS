# print('start')

# for i in range(1,10):
#     pass

# print('end')

# else clause with loops
for i in range(2,5):
    if i%3==0: break
    print(i)
else: # only if loop completes the iterations and is not exited by break
    print('else clause')

ccno = 12345
temp = ccno
search = int(input('enter a value to search'))
while temp!=0:
    digit = temp%10
    if digit == search:
        print(search,'found')
        break
    temp = temp//10
else:
    print(search, 'not found')
