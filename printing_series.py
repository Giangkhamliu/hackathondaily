# Write a program to add first n terms of the following series using a while loop :
# 1/1! + 1/2! + 1/3! + …….. + 1/n!
n=int(input("Enter the number:-"))
i=1
s=""
while i<=n:
    s+="1/"+str(i)+"!+"
    i+=1
print(s[0:-1])