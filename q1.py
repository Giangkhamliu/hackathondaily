 #1.Problem (question name-Divisibility)
a=int(input("Enter the number of array? "))
i=0
n1=""
while i<a:
    num=int(input("Enter the number :-"))
    n=num%10
    n1+=str(n)
    i+=1
if int(n1)%10==0:
    print(n1,"is divisible by 10")
else:
    print(n1,"is not divisible by 10")