s1={} # it is a dictionary
s1 = set()
s1 = {1,2,36,1,23,56,34,89,90}
# print(type(s1))
# print(s1)
# print(len(s1))
# print(max(s1))
# print(min(s1))
# print(sum(s1))
# print()
# for i in s1:
#     print(i, i*i)

# s1.add(100)
# print(s1)
# s1.update({2,3,4,5,6,7})
# print(s1)
# s1.discard(340)
# print(s1)
# # s1.remove(1000)
# print(s1)

a = {1,2,3,4,5,6}
b = {2,3,7,8,9}
print(a, b)
# union -> all common and uncommon elements from both the set
print(a.union(b))
print(b.union(a))
print(a|b)
print()
# intersection => common elements
print(a.intersection(b))
print(b.intersection(a))
print(a&b)
print()
# difference -> includes element of 1st set not in 2nd set
print(a.difference(b))
print(a-b)
print(b.difference(a))

print()
# symmetric difference -> all uncommon elements from both sets
print(a.symmetric_difference(b))
print(b.symmetric_difference(a))
