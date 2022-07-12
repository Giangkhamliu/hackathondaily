## Finding the pairs
l=[10,20,30,50,30,20,10,10,20,20,10]
l1=[]
for i in l:
    if i not in l1:
        l1.append(i)
b=[]
for j in l1:
    c=0
    k=0
    for k in l:
        if j==k:
            c+=1
    b.append(c)
sum=0
for m in b:
    a=m//2
    sum+=a
print(sum)



# l1=[]
# i=0
# while i<len(l):
#     if l[i] not in l1:
#         l1.append(l[i])
#     i+=1
# j=0
# b=[]
# while j<len(l1):
#     c=0
#     k=0
#     while k<len(l):
#         if l1[j]==l[k]:
#             c+=1
#         k+=1
#     b.append(c)
#     j+=1
# m=0
# sum=0
# while m<len(b):
#     a=b[m]//2
#     sum+=a
#     m+=1
# print(sum)