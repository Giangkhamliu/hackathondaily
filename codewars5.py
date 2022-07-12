# 1
# 1*2
# 1**3
# 1***4
# 1****5

n=int(input("Enter the number:- "))
i=0
b=1
x=1
while i<n:
    a="*"*i
    if b==1:
        print(b)
    else:
        print(str(x)+a+str(b))
    i+=1
    b+=1
    