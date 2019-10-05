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
#This program displays the number of ages that are higher 
#than 60 and the sum of the ages that are less than 20
##########################################################


count = 0
sumOfAges = 0

with open("ages.dat","rt") as file:
    for line in file:
        line = int(line) 
        listing = []
        listing.append(line)
    
        for allline in listing: 
        
        #print(allline)
            if allline > 60:   
                count += 1
            elif allline < 20:
                sumOfAges += allline                                    
    print("Total number of people who are above the age of 60 are :", count)
    print ("The sum of age of people who are below 20 is: ", sumOfAges)
    
    #print(line)
    
           
    
    

    
    




