#19. Adding and removing dots
def add_dot(s):
    i=0
    b=""
    while i<len(s):
        a=s[i]+"."
        b=b+a
        i+=1
    print(b[0:-1])
    def remove_dot(s):
        i=0
        b=""
        while i<len(s):
            if s[i]!=".":
                b+=s[i]
            i+=1
        print(b)
    s=input("Enter the string to remove dot:-")
    remove_dot(s)
s=input("Enter the string to add dots:-")
add_dot(s)
