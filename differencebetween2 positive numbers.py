
#2 WAP to read 2 distinct integer be sure the program will print 6 both when 9 and 15 are read. Program
#will display difference  between 2 positive numbers, regardless of which one is larger

firstNumber =int(input("Enter first number"))
secondNumber =int(input("Enter first number"))

if firstNumber > secondNumber:
    difference = firstNumber - secondNumber
    print("The difference is between the number is", difference)
else:
    difference =secondNumber -firstNumber
    print("The difference is between the number is ", difference)    