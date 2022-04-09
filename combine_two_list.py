a=[1, 2, 3, 4, 5]
b=[10,9,8,7,6]
i=0
while i<len(a):
    if a[i] not in b:
        b.append(a[i])
    i+=1
b.sort()
print(b)
