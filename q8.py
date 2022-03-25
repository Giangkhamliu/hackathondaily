# 8.Car or Bus
t=int(input("Enter the no. of test cases :-"))
i=0
while i<t:
    x=int(input("Enter the minutes that a bike takes:-"))
    y=int(input("Enter the minutes that a Car takes:- "))
    if x>y:
        print("He will travel by Car")
    elif x<y:
        print("He will travel by Bike")
    elif x==y:
        print("Same")
    i+=1
