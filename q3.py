#3.Problem (Problem Code: FBC, fill the buckets)

T=int(input("Enter the no. of test cases:- "))
i=0
while i<T:
    k=int(input("Enter the maximum amount of litres:-"))
    x=int(input("Enter the litres that is filled:- "))
    print(k,x)
    y=k-x
    print("The amount of water that can fill without overflowing:-",y)
    i+=1