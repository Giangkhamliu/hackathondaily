# Take an array and remove every second element from the array. Always keep the 
# first element and start removing with the next element.
# Example:
# ["Keep", "Remove", "Keep", "Remove", "Keep", ...] --> ["Keep", "Keep", "Keep", ...]
# None of the arrays will be empty, so you don't have to worry about that!

def remove_every_other(my_list):
    l=[]
    i=0
    while i<len(my_list):
        if i%2==0:
            l.append(my_list[i])
        i+=1
    return l
print(remove_every_other([1,2,3,4,5,6,7,8,9,10]))
