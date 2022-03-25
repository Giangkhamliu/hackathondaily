#14. Power of Four
def power(n):
    if n%4==0 or n==1:
        return True
    else: 
        return False
n=int(input("Enter the number:-"))
print(power(n))
