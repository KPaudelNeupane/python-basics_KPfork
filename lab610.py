##################################################
## Author: Subash Neupane
## Copyright: Copyright 2019, Lab 6
## Date: September, 2019
## Credits: Subash Neupane
## License: GPL
## Version: 1.0
## Mmaintainer: Subash Neupane
## Email: sneupane2127@tuskegee.edu
## Status: Production
##################################################


# a.	The program displays the number of records processed 
# and the total wages paid to the employees.

with open("wages.dat", "rt") as file:
    def wageAndRecords():
        count = 0
        totalWages = 0 #this is totalWage ( hours * hourly wage)
        hourlyEight = 0
        sumOfWages = 0
        wageHigherthan300 = 0
        highestWage = 0
        for line in file:
            seprateHourAndWage = line.split(",") #removes comma between number of hours and wages
            hoursIndex = seprateHourAndWage[0] #storing hours 
            wageIndex = seprateHourAndWage[1] #storing wages
            hourAsInteger = int(hoursIndex) #converting hours string into integer
            wagesAsFloat = float(wageIndex) #converting hourly rate into float
            
            if hourAsInteger == -1:
                break
            count += 1
            wages = hourAsInteger * wagesAsFloat
            totalWages += hourAsInteger * wagesAsFloat
            sumOfWages += wagesAsFloat
            avgWage = sumOfWages/count  
            
            if wagesAsFloat > 8.00:
                hourlyEight += 1
            if wages > 300:
                wageHigherthan300 += 1 
            # for i in wages:
            #     maximumwage = max(i)
            if highestWage >= wages:
                highestWage = highestWage
            elif highestWage < wages:
                highestWage = wages   
        
        print("The total number of records processed is ", count)
        print("The total wages paid to the employee is ", totalWages)
        print("The total number of employees with hourly wage higher than $8.00 is ",hourlyEight)
        print("The average hourly wage of all employees is ", avgWage) 
        print("The number of employees who made higher than $300.00 last week is ",wageHigherthan300)
        print("The highest wage paid to the employee is", highestWage)     
    wageAndRecords()
file.close()            
            
            

        
    
   