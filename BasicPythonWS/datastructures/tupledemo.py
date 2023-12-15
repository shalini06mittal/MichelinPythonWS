# # # () immutable
# # t1 = (1,2,3,4,4,2,3,6,7,8)
# # print(type(t1))
# # print(t1)
# # print(t1[0])
# # print(t1[-1])
# # print(t1[0:2])
# # print(len(t1))
# # print(max(t1))
# # print(min(t1))
# # print(sorted(t1))

# # # t1[0]= 100
# # print(t1.index(4))
# # print(t1.count(2))

# # vowels= tuple('aieou')
# # print(type(vowels))
# # print(vowels)

# # vowels = 10

# # t1 = (1,2,3,4,4,2,3,6,7,8)
# # t2 = (1,2,3,4,4,2,3,6,7,8)
# # t3 = (1,2,3,4,4,2,3,6,7,9)
# # t4 = (1,2,3,4,4,2,3,6,8)
# # # it compares element by element starting fron the first until a difference is found
# # print(t1==t2)
# # print(t1==t3)
# # print(t1==t4)
# # print(t2<t4)
# # t5 = t1+t2
# # print(t5)
# # print((1,2)*3)
# # print(1 in t1)
# # print(1 not in t1)

# # data = ('red','yellow', 'green')
# # for d in data:
# #     print(d.upper())

# # 2 dimensions
# population = (
#    # India, USA, China, Japan, Australia 
#     (1,2,3,5,6), #0 23
#     (7,8,45,9,10), #1 22
#     (23,34,50,54,78), #2 21
#     (90,80,70,60,50) #3 20
# )
# # print average/ total of population in every year
# # print totol for each country

# #Columnwise Total 
# totalindia = 0
# totalUSA = 0
# totalChina = 0
# totalJapan = 0
# totalAustralia = 0
# for i in range(0,len(population)):
#     totalindia = totalindia + population[i][0]
#     totalUSA = totalUSA + population[i][1]
#     totalChina = totalChina + population[i][2]
#     totalJapan = totalJapan + population[i][3]
#     totalAustralia = totalAustralia + population[i][4]
# print('totalindia', totalindia)
# print('totalUSA', totalUSA)
# print('totalChina', totalChina)
# print('totalJapan', totalJapan)
# print('totalAustralia', totalAustralia)

# #Rowwise total and avg
# total23 = 0
# total22 = 0
# total21 = 0
# total20 = 0
# for i in range(0,len(population[0])):
#     total23 = total23 + population[0][i]
#     total22 = total22 + population[1][i]
#     total21 = total21 + population[2][i]
#     total20 = total20 + population[3][i]
# print('total23', total23)
# print('total22', total22)
# print('total21', total21)
# print('total20', total20)
# print('avg23', total23/5)
# print('avg22', total22/5)
# print('avg21', total21/5)
# print('avg20', total20/5)

# print(len(population))
# print(population[0][3])
# print(population[0:3])


# t = (1)
# print(type(t))
# packing
colors = 'red','brown','green'
# unpacking
# c1, c2, c3,c4 = colors
# print(c1, c2)

n_tuple = (1,
           "mouse", 
           [8, 4, 6], 
           (1, 2, 3))
for row in n_tuple:
    #print(row)
    if type(row) == int:
        print(row **4)
    elif type(row) == str:
        print(row.upper(), ' is string')
    else:
        sum = 0
        for column in row:
            sum += column
        print(sum)

print(n_tuple)
del n_tuple
# print(n_tuple)

t1=('',(4,5,6),(7,8,9))
print(all(t1))
print(any(t1))
# nos = (1,2,3,4,5)
# for v in nos:
#     print(v)