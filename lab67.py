########################################################
## Author: Subash Neupane
## Copyright: Copyright 2019, Lab 6
## Date: September, 2019
## Credits: Subash Neupane
## License: GPL
## Version: 1.0
## Mmaintainer: Subash Neupane
## Email: sneupane2127@tuskegee.edu
## Status: Production
#########################################################
######****** PROGRAM DESCRIPTION **************##########
#This program calculates and returns the area of the 
# triangle made up by the given three lengths
##########################################################


from math import sqrt

length1 = int(input("Enter the length of first side "))
length2 = int(input("Enter the length of second side "))
length3 = int(input("Enter the length of third side "))

def computeArea(length1,length2,length3):
    length1 =float(length1)
    length2 =float(length2)
    length3 =float(length3)
    
    s = (length1+length2+length3)/2
    
    #areaOfTriangle = (s*(s-length1)*(s-length2)*(s-length3)) ** 0.5
    areaOfTriangle = sqrt((s*(s-length1)*(s-length2)*(s-length3)))
    areaOfTriangle = round(areaOfTriangle,2)
    #print('The are of given triangle is ', round(areaOfTriangle,2)) #
    return(areaOfTriangle)
    
print("The area of the triange is ", computeArea(length1,length2,length3))

    