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
#This program  reads alpha, number and other characters in
# a given string
##########################################################


seq = input("Enter the String of len exactly 20 :") #Enter a sequence
alpha   = ""
number  = ""
special = ""

if len(seq) != 20:
    print("Please enter string of length exactly 20")
else:
    for i in range(len(seq)):
    
        if (seq[i].isdigit()): #calling in built method to check numbers in the string
            number += seq[i]
        elif(seq[i].isalpha()): #calling in built method to alpha numbers in the string
            alpha += seq[i]
        else:
            special += seq[i]
        #About13:24:43p.m.111
    print("Number of letters:  ",len(alpha))       
    print("Number of digit characters: ",len(number)) 
    print("Other characters: ",len(special))     

#End of Program        
    

          

        
    

    
    
