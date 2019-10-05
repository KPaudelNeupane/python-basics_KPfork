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
#This program converts and returns the total number of 
# seconds based on the given time
##########################################################

hours = int(input("Enter the number of hours "))
minutes = int(input("Enter the numbe of minutes "))
seconds = int(input("Enter the number of seconds "))

def getTime(hours,minutes,seconds):
    
    hourIntoSecond = int(hours * 60 *60)
    minutesIntoSecond = int(minutes *60)
    
    totalTime = hourIntoSecond + minutesIntoSecond + seconds
    
    return totalTime
     #for checking purposes
     
print(getTime(hours,minutes,seconds))     
    
    