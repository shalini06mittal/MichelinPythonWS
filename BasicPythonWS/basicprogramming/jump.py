# break and continue
# break is used to stop the loop in between conditionally
for i in range(1,11):
    print(i)
    if i==5:
        break

# 9898 2132 1232 4567
'''
1*100+2*10+3*1 = 123
123%10 = 3
123/10 = 12
12%10 = 2
12/10 = 1
'''
ccno = 12345
temp = ccno
search = int(input('enter a value to search'))
isFound = 0
while temp!=0:
    digit = temp%10
    if digit == search:
        print(search,'found')
        isFound =1
        break
    temp = temp//10
if isFound == 0:
    print(search, 'not found')


# continue => skip the processing for that iteration
for i in range(1,20):
    if i%5==0:
        continue
    print(i)
    






