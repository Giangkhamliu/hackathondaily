n=input("Enter the brackets:-")
a1=0
a2=0
b1=0
b2=0
c1=0
c2=0
i=0
while i<len(n):
    if n[i]=="(":
        c1=c1+1
    elif n[i]==")":
        c2=c2+1
    elif n[i]=="{":
        b1=b1+1
    elif n[i]=="}":
        b2=b2+1
    elif n[i]=="[":
        a1=a1+1
    elif n[i]=="]":
        a2=a2+1
    i=i+1
if a1==a2 and b1==b2 and c1==c2:
    print(True)
else:
    print(False)

