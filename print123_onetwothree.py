n=input("Enter the number:-")
l=["zero","one","two","three","four","five","six","seven","eight","nine"]
s=""
i=0
while i<len(n):
    j=0
    while j<len(l):
        if n[i]==str(j):
            s+=" "+l[j]
        j+=1
    i+=1
print(s)