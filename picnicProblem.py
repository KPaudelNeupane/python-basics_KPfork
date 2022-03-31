
#1.	Two families meet at a park for a picnic. At the end of the day one family travels east at an average speed of 42 miles 
# per hour and the other travels west at an average speed of 50 miles per hour. Both families have approximately 160 miles to travel.
#1.	Find the time it takes each family to get home.
#2.	Find the time that will have elapsed when they are 100 miles apart.
#3.	Find the distance the eastbound family has to travel after the westbound family has arrived home.


speedOfFamilyOne = 42
speedOfFamilyTwo = 50
totalDistance = 160

timeTakenByFamilyOne = float(totalDistance/ speedOfFamilyOne)
print("Time taken by family one is ", timeTakenByFamilyOne, "hrs")

timeTakenByFamilyTwo = float(totalDistance/speedOfFamilyTwo)
print("Time taken by family two is ", timeTakenByFamilyTwo, "hrs")

elapsedDistance = 100

timeWhen100milesApart = float(elapsedDistance/(speedOfFamilyOne + speedOfFamilyTwo))
print("Time elapsed when they are 100 miles apart is ", timeWhen100milesApart)

remainingDistanceEastboud = float(totalDistance - (timeTakenByFamilyTwo * (speedOfFamilyOne)))
print("The time taken by family going inbound when family going west bound reach home is ", remainingDistanceEastboud, "miles")

##2.	Mary needs to calculate the distance between two points in the Cartesian coordinate system. 
# Each point in the system is represented by a pair of real values denoted by (x, y). 
# Write a program to help her find the distance between two points. The program first reads two points; 
# then it calculates and prints the distance between these two points. A sample run of the program looks like:
#•	Enter the x value of the first point: 2.0
#•	Enter the y value of the first point: -1.0
#•	Enter the x value of the second point: 5.0
#•	Enter the y value of the second point: 3.0
#•	The distance between (2.0, -1.0) and (5.0, 3.0) is 5.0.

from math import sqrt
firstPoint = float(input("Enter the value of first point "))
secondPoint = float(input("Enter the value of second point "))
thirdPoint = float(input("Enter the value of third point "))
fourthPoint = float(input("Enter the value of fourth point "))

distanceBetwweenPoints = sqrt((thirdPoint - firstPoint) **2 + (fourthPoint-secondPoint)**2)
print("The distance between (2.0, -1.0) and (5.0, 3.0) is ,", distanceBetwweenPoints )


#Bi-City Decor has a special sale on its top-of-the-line carpet. Mr. Woods wants to buy a piece of carpet to cover a floor. 
# The store charges for stitching the sides of a piece of carpet. The tax rate is 7.5 percent. Write a program to read the 
# sale price of the carpet ($ per square yard), the length and the width of the floor (in feet), and the stitching fee for 
# each linear foot. Compute and print the cost of the carpet, stitching cost, sales tax, and amount due for Mr. Woods if
#  he decides to buy the carpet from the store? Display the result to 2 decimal places. A sample run is given below:
# •	Enter the cost of carpet per square yard: 12.00
# •	Enter the length of the carpet (in feet): 20.00
# •	Enter the width of the carpet (in feet): 4.50
# •	Enter the stitching fee per linear foot: 1.00
# •	The cost of the carpet = 120.00
# •	The stitching fee = 49.00
# •	Sales tax = 10.84
# •	Amount due = 155.34

taxRate = 7.5 
costOfCarpetInYard = 12
lengthOfCarpet = 20
widthOfCarpet = 4.50
stitchingLinearFeet = 1

areaOfCarpetInSqFeets = (lengthOfCarpet * widthOfCarpet)
#print(areaOfCarpetInSqFeets)

areaOfCarpetInSqYard = areaOfCarpetInSqFeets *0.111111113


totalCostOfCarpet = round((areaOfCarpetInSqYard * costOfCarpetInYard),2)
print("Total Cost of the carpet is ", totalCostOfCarpet)

stitchingCost = (2 * (lengthOfCarpet + widthOfCarpet)) * stitchingLinearFeet
points = round(stitchingCost,2)
print("Stitching Cost is ", points)


#4. Julie works at the check-out counter at one of Wal-mart stores. Handing changes (the amount less than a dollar in coins) back to 
# customers is not a trivial chore to her. You are asked to write a program to help her out. The program prompts for an integer that 
# represents the amount of change (in cents) to be handed back to a customer. The program then determines and prints the minimum number 
# of half dollars, quarters, dimes, nickels, and pennies that will make the correct change. A sample run of the program is given below:
# •	Enter change [0..99]: 83
# •	The minimum number of coins to return 83 cents are
# •	Half(ves): 1
# •	Quarter(s): 1
# •	Dime(s): 0
# •	Nickel(s): 1
# •	Penny(ies): 3


change = int(input("Enter Change "))

halves = 0
quarters = 0 
dimes = 0 
nickles = 0
penny = 0
amount = 0

while change > 0 and change <99:   
    if change >= 50 and change <99:
        halves += 1
        change -= 50
    elif change >= 25 and change <50:
        quarters += 1
        change -= 25
    elif change >=10 and change <25:
            dimes += 1
            change -= 10
    elif change >= 5 and change <10:
        nickles += 1
        change -= 5        
    else:
        penny += 1
        change -= 1
             
print(halves,quarters, dimes,nickles, penny)                
          
    


     

