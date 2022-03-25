#16. Minimum Index Sum of Two Lists
list1 = ["Shogun","Tapioca Express","Burger King","KFC"]
list2 = ["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]
list1 =["Shogun","Tapioca Express","Burger King","KFC"]
list2 = ["KFC","Shogun","Burger King"]
i=0
a=[]
while i<len(list1):
    j=0
    while j<len(list2):
        if list1[i]==list2[j]:
            a1=list1[i]
            a.append(a1)
        j+=1
    i+=1
b=[]
if len(a)>1:
    b.append(a[0])
    print(b)
else:
    print(a)
# Output: ["Shogun"]
# Explanation: The restaurant they both like and have the least index sum is "Shogun" with index sum 1 (0+1).

