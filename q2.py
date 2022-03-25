#2. Problem Code: BATTERY LOW
T=int(input("Enter the number of cases to be check? "))
i=0
while i<T:
    cases=int(input("Enter the battery percentage? "))
    if cases<=15:
        print("Yes,  The battery is low")
    else:
        print("No , The Battery is not low")
    i+=1