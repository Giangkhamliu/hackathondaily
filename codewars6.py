l=[[1,3,4],[5,4,6],[6,1]]
i=0
s=0
while i<len(l):
    j=0
    while j<len(l[i]): 
        if i==0:
            s+=l[i][j]
        else:
            s+=l[i][-1]
            break
        j+=1
    i+=1
print(s)