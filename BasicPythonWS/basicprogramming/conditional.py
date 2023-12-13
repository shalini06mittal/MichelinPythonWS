'''
conditional programming
calculator
+
-
if op is + perform addition
if op is - perform sub
op == '+'
'''
# + or -
op = input('Choose either operator: + - :\n')
 
n1 = int(input('enter a number'))
n2 = int(input('enter a number'))
# if op == '+':
#     print(n1 + n2)

# if op == '-':
#     print(n1 - n2)
# $
if op == '+':
    print(n1 + n2)
elif op == '-':
    print(n1 - n2)
elif op == '*':
    print(n1 * n2)
elif op == '/':
    print(n1 / n2)
else:
    print('wrong operator')
