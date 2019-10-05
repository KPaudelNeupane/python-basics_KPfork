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
#This program  determine custom ratings for scaled score 
# between 1-10
##########################################################

rating_score = int(input("Please enter score on the scale of 1-10  :"))

def determineRating(rating_score):
    
    gradeP = "P"
    gradeA = "A"
    gradeG = "G"
    if rating_score >= 1 and rating_score<=3:
       # print("Your rating is ", gradeP)
        return gradeP
    elif rating_score >=4 and rating_score <=6:
        #print("Your rating is ", gradeA)
        return gradeA
    elif rating_score >= 7 and rating_score <=10:
       # print("Your rating is", gradeG)
        return gradeG
    else:
        return "The number is out of range"    
print("Your grade for your score ",rating_score, "is" , determineRating(rating_score))  #Calling function

#End of Program