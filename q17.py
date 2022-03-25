#17. Capital indexes
def capital_index(s):
    i=0
    a=[]
    while i<len(s):
        if s[i].isupper():
            index=i
            a.append(index)
        i+=1
    return a
s=input("Enter any string:-")
print(capital_index(s))



