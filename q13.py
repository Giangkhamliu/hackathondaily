#13. Move zero
num=[0,1,0,3,12]
n=len(num)
count = 0
i=0
while i<n:
    if num[i]!= 0:
        num[count] =num[i]
        count+=1
    i+=1
while count < n:
    num[count] = 0
    count += 1
print(num)