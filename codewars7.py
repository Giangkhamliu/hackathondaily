def two_sum(number,n):
    x=[]
    i=0
    while i<len(number):
        j=0
        while j<len(number):
            sum=number[i]+number[j]
            if sum==n and (number[i]<number[j]):
               x.append((i,j))
            j+=1
        i=i+1
    print(x)
n=5
number=[1,2,3,4,5]
two_sum(number,n)