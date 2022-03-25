#20 min-maxing
l1=[1, 2, 3]
def min_maxing(l1):
    i=0
    lar=0
    sml=l1[0]
    while i<len(l1):
        if l1[i]>lar:
            lar=l1[i]
        elif l1[i]<sml:
            sml=l1[i]
        i+=1
    mm=lar-sml
    return mm
print(min_maxing(l1))