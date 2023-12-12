# to print table/ multiples of a number
# no = int(input('enter a no')) # 5
# 5 10 ... 50
'''
1 2 3 4 5 6 7 8 9 10
2 4 6 8 ..
3 6 9 12 ....
4 8 12 16 ....
5.....
'''
# for no in range(1,6):# no = 2
#     for v in range(1,11):
#         print(no * v, end=' ')
#     print()

for i in range(5):
    for j in range(3):
        if i==j: break
        print(i,j)

