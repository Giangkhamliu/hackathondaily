def create_phone_number(n):
    a=""
    b=""
    c=""
    d=""
    i=0
    while i<len(n):
        if i<3:
            a+=str(n[i])
        if i>2 and i<5:
            b+=str(n[i])
        if i==5:
            c+=str(n[i])+"-"
        if i>5:
            d+=str(n[i])
        i+=1
    print("("+a+")",b+c+d)
create_phone_number([1,2,3,4,5,6,7,8,9,0])
create_phone_number([9,8,6,3,0,9,3,3,0,7])