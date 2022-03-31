#1.	Two families meet at a park for a picnic. At the end of the day one family travels east at an average speed of 42 miles 
# per hour and the other travels west at an average speed of 50 miles per hour. Both families have approximately 160 miles to travel.
#1.	Find the time it takes each family to get home.
#2.	Find the time that will have elapsed when they are 100 miles apart.
#3.	Find the distance the eastbound family has to travel after the westbound family has arrived home.


speedFamilyOne = 42
speedFamilyTwo = 50
totalDistance = 160

timeForFamilyOne = float(totalDistance / speedFamilyOne)

print(timeForFamilyOne)
timeForFamilyTwo = totalDistance / speedFamilyTwo
print(timeForFamilyTwo)

elapsedDistance = 100

remainingTime = float(elapsedDistance/(speedFamilyOne+speedFamilyTwo))
print(remainingTime)

remainingDistEastBound = float(totalDistance-((timeForFamilyTwo)*speedFamilyOne))

print(remainingDistEastBound)




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


#1 sq foot  = 0.1113 Sq yard


taxRate = 7.5

cost = int(input("Enter cost of carpet "))
length = int(input("Enter length of the carpet "))
width = float(input("Enter width of carpet "))
stitchFee = int(input("Enter stitching fee "))

areaOfCarpet = round(((length * width) * 0.11113),2) #multiplyting by 0.11 for sq feet conversion to sq yards 

totalCost = round((areaOfCarpet * cost),2)
print("The cost of carpet is ",totalCost)

stitchingCost = round((((length + width) *2) * stitchFee),2)
print("Stitching Fee = ", stitchingCost)

finalCost = totalCost + stitchingCost

salesTax = (taxRate/100) * finalCost
print("Sales Tax = ",salesTax)

amountDue = salesTax + finalCost
print("Amount Due = ",amountDue)



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


change1 = int(input("Enter the amount in cents between 0 and 99 "))

halves = 0
quarter = 0 
dimes = 0 
nickles = 0
penny = 0

change = change1
while change > 0 and change < 100:
    if change > 50 and change <100:
        halves += 1
        change -= 50
    elif change > 25 and change < 50:
        quarter += 1    
        change -= 25
    elif change > 10 and change <25:
        dimes += 1
        change -= 10 
    elif change >5 and change <10:
        nickles += 1
        change -= 5
    else: 
        penny += 1
        change -= 1    
print(halves, quarter, dimes, nickles,penny)        
        
   
        