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
#This program calculates premium based on gender and age
##########################################################


age = int(input("Enter the age of the person "))
gender = input("Enter gender : ")
def computePremium(age,gender):
    
    if age < 25 and gender == "m":
        premium = 2500
        return premium
       
    elif age >= 25 and gender == "m":
        premium = 700
        return premium
       
    if age < 21 and gender == "f":
        premium = 800
        return premium
       
    elif age>= 21 and gender =="f":
        premium = 500
        return premium 
       
        
print("The premium for age",age, " and gender", gender, " is", computePremium(age,gender))           
            
            
#End of the program    