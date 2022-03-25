#18. Middle letter
def mid(s):
    n=len(s)
    if n%2!=0:
        middle=int(n/2)
        a=(s[middle])
        return a
    else: 
        return ("empty")
s=input("Enter the string:-")
print(mid(s))