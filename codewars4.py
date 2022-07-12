s=input("Enter the string:-")
d={}
a=[]
i=0
while i<len(s):
    c=0
    j=0
    while j<len(s):
        if s[i]==s[j]:
            c+=1
            b=s[i]
        j+=1
    i+=1
    if c==1:
        a.append(b)
i=0
while i<len(s):
    if a[0]==s[i]:
        x=i
    i+=1
d[str(a[0])]=str(x)
print(d)