#5.Chef and Chocolates
t=int(input("Enter the no. of test cases :-"))
i=0
while i<t:
    c=int(input("Enter the no. of chocolates he wants to give:-"))
    x=int(input("Enter the no. of chocolate he has with him:- "))
    y=int(input("Enter the price of per chocolate   :-"))
    z=(c-x)*y
    print(z)
    i+=1
