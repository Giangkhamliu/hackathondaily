#22. Palindrome
def palidrome(string):
    s=string.upper()
    s1=""
    i=-1
    while i>=-len(s):
        s1+=s[i]
        i-=1
    if s==s1:
        return True
    else:
        return False
s=input("Enter the strings:-")
print(palidrome(s))