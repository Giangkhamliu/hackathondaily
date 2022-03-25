#15. Add Two Numbers
l1 = [7,2,4,3]
l2 = [5,6,4]
def add_two(l1,l2):
        a=[]
        l=""
        m=""
        i=0
        while i<len(l1):
            l+=str(l1[i])
            i+=1
        i=0
        while i<len(l2):
            m+=str(l2[i])
            i+=1
        sum=int(l)+int(m)
        a.append(sum)
        return a
print(add_two(l1,l2))
