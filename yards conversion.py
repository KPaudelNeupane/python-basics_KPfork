#WAP conversion table


lb = int(input("Enter lower bound "))
up = int(input("Enter Up bound "))
topBound = up + 1


#1 yard = 36 inches
for i in range(lb, topBound):
    conversion = i * 36
    print(i, conversion)
    