f1 = open('test.txt')
# reads the entire file contents as a string
# data = f1.read()
# reads only 1 single line
# while True:
#     data = f1.readline()
#     if data == '':
#         print('end of file')
#         break
#     print(data)
print(f1.tell())
f1.seek(10)
print(f1.tell())
data = f1.readlines()
print(data)
print(type(data))
f1.close()

# print(data.splitlines())

