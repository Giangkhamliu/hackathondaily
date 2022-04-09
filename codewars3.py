# Given the a list of numbers, return the list so that the values increment by 1
#  for each index up to the maximum value.
def numbers(a):
    a1=a[-1]
    l=[]
    i=a[0]
    while i<=a1:
        l.append(i)
        i+=1
    print(l)
numbers([1, 2, 13])
numbers([-4,4,5])



# or
def numbers(a):
    s=a[0]
    b=0
    i=0
    while i<len(a):
        if a[i]>b:
            b=a[i]
        if a[i]<s:
            s=a[i]
        i+=1
    l=[]
    while s<=b:
        l.append(s)
        s+=1
    print(l)
numbers([-4,4,5])
numbers([2,5,7,9,1])
numbers([-1,4,7,9])
