def odd_dash(l):
    l1=str(l)
    s=""
    i=0
    j=i+1
    while i<len(l1) and j<len(l1):
        if int(l1[i])%2!=0 and int(l1[j])%2!=0:
            s+=l1[i]+"-"
        else:
            s+=l1[i]
        i+=1
        j+=1
    print(s+l1[-1])
odd_dash(123579)
odd_dash(13579)
odd_dash(2468)
odd_dash(1234578)




