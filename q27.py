#27. Length of Number
# Create a function that takes a number num and returns its length.
# Examples
# number_length(10) ➞ 2
def function(num):
    a=len(str(num))
    return a
num=int(input("Enter the number:-"))
print(function(num))