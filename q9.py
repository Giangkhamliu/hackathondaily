#9.Good Program
t=int(input("Enter the no. of test cases :-"))
i=0
while i<t:
    n=int(input("Enter the no. of bytes taken:-"))
    if n%4==0:
        print("GOOD")
    else:
        print("NOT GOOD")
    i+=1