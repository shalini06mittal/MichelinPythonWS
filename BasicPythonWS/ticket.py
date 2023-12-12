'''
Print total amount for the tickets purchased
Assume following conditions
age<=5 free
age >5 and <=15 150/-
age > 15 250/-
Ask the user to enter 
1. name
2. tickets for how many people
3. for each person, age 
 print the total amount the customer needs to pay

NESTED LOOP:
Continue the above process for different customers,
until admin enters exit
and also print the total amount each customer has to pay.

'''

quit=0
price=0
while(quit!=1):
    input('Enter name :')
    no=int(input('Enter number of people : '))
    price=0
    for i in range(1,no+1):
        input('Enter name of person 1:')
        age=int(input('Enter age of person : '))
        if age>5 and age<=15:
            price+=150
        elif age>15:
            price+=250
    print('Total amount to be paid : ',price)
    quit=int(input('If you want to exit press 1 , else enter other number:'))