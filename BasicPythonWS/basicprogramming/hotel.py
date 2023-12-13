'''
Occupancy rate = number of rooms occupied /total number of rooms
Write a program  that calculates the occupancy rate for your hotel. 
•	Start by asking the number of floors in the hotel. 
•	A loop should then iterate once for each floor. 
o	During each iteration, the loop should ask the user for 
	the number of rooms on the floor, and 
	the number of those rooms occupied. 
•	After all the iterations, the program should display
o	 the number of rooms in the hotel, 
o	the number of occupied rooms, 
o	the number of vacant rooms, and 
o	the occupancy rate for the hotel 
Input Validation: 
•	Do not accept a value less than 1 for the number of floors. 
•	Do not accept a number less than 10 for the number of rooms on a floor. 
•	Do not accept a number of rooms occupied than are on the floor. 
•	(You need THREE validation loops).

'''
floors = int(input('Enter No of floors '))
while floors < 1:
    floors = int(input('Please enter number of floors greater than 0'))   
totalrooms = 0
totaloccupied = 0
for i in range(1, floors+1):         
    print('Floor',i)
    noofrooms = int(input('No of rooms on the floor '))
    while noofrooms < 10:        
        noofrooms = int(input('Please enter number of rooms greater than 10 '))            
    totalrooms = totalrooms + noofrooms
    noofoccrooms = int(input('No of occupied rooms on the floor '))
    while noofrooms < noofoccrooms: 
        noofoccrooms = int(input('Please enter occupied rooms less than eq to number of rooms on the floor '))
    totaloccupied = totaloccupied + noofoccrooms
print('Total rooms ',totalrooms)
print('Total occupied rooms ',totaloccupied)

