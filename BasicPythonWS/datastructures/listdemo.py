
l1 = [1,2,3,4,5,1]
# print(type(l1))
# print(sum(l1))
# print(max(l1))
# print(min(l1))
# print(len(l1))
# print(a(l1)

#methods
# print(l1.count(1))
# print(l1[4])
# l1[4] =100
# print(l1)

#[12.34,23,32,45.7]
scores = [20, 12, 8,9,10, 9]
# print(sorted(scores))
# scores.sort(reverse=True)
# print(scores)
# # scores.
# names =['shalini','shreya','ajay','leanne','saikarnika']
# names.sort(key=len)
# print(names)
# print(sorted(names))
scores.append(15)
# print(scores)
# without flattening the values
# scores.append([1,2,3])
# [20, 12, 8, 9, 10, 15, [1, 2, 3]]
# print(scores)
# scores.extend([1,2,3])
#[20, 12, 8, 9, 10, 15, 1, 2, 3]
# print(scores)
# scores.remove(9) # takes value to remove and removes first occurence from the list
# print(scores)
# del scores[3] # takes index from the list to remove a value
# print(scores)

# scores.insert(2, 100)
# print(scores)

# s1 = scores
# print(s1)
# s1.append(500)
s1 = scores.copy() # shallow copy
s1.append(500)
# print(s1)
# print(scores)

# n1 = [4, [1,2,3],[4,5,6]]
# n2 = n1.copy()
# n1[0] = 400
# print(n1, n2)
# n2[1][1] = 20
# print(n1, n2)

# built in module
import copy
n1 = [4, [1,2,3],[4,5,6]]
n2 = copy.deepcopy(n1)
n1[0] = 400
# print(n1, n2)
# n2[1][1] = 20
# print(n1, n2)
# print(scores)
# print(scores.pop())
# print(scores)
# print(scores.pop(1))
# print(scores)

'''
Create an empty list.
ask the user how many phonenos to be added in the list
take those many phone nos as input and add in the list
ask the user for a phone number to search in the list
print found or not found based on the result
'''

# number_of_phonenumbers = int(input('Enter the number of phone numbers to be added'))

# a= list()
# a=[]
# for i in range(0,number_of_phonenumbers):
#     a.append(int(input('Enter number ')))
# number_to_be_found = int(input('Enter the number to be found '))

# if number_to_be_found in a:
#     print('found')
# else:
#     print('not found')

# for j in range(number_of_phonenumbers):
#     if a[j]==number_to_be_found:
#         print('found')
#         break
# else:
#     print('not found')

# OPERATORS

l1 = [1,2,3]
l2 = [4,5,6]
l3 = l1+l2
print(l1)
print(l2)
print(l3)

print(l1*3)

del l3[0:1]
print(l3[0:1])
# l3= l1+5