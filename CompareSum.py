#WAP compareSum

import math

def compareSum(myTuple):
    
    firstFive = myTuple[:5]
    secondFive =myTuple[-5:]
    
    sumFirstFive = sum(firstFive)
    sumSecondFive = sum(secondFive)
    
    if sumFirstFive >  sumSecondFive:
        print("Sum of first five is greater")
    elif sumFirstFive == sumSecondFive:
        print("No difference")    
    else: 
        print("Sum of second five is greater")     
        

myTuple = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15)

print(compareSum(myTuple))    