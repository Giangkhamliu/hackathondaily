# 10.Counting Pretty Numbers Problem Code: NUM239
t=int(input("Enter the no. of test cases :-"))
j=0
while j<t:
    x=int(input("Enter the starting number-"))
    y=int(input("Enter the ending number:- "))
    count=0
    a=[]
    while x<=y:
        a.append(x)
        x+=1
    print(a)
    i=0
    while i<len(a):
            if x>9:
                a1=a[i]%10
                if a1==2 or a1==3 or a1==9:
                    count+=1
            else:
                if a[i]==2 or a[i]==3 or a[i]==9:
                   count+=1
            i+=1
    print(count)
    j+=1