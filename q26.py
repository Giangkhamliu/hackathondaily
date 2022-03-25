#26. Convert Minutes into Seconds
# Write a function that takes an integer minute and converts it to seconds.
# Examples
# convert(5) ➞ 300
# convert(3) ➞ 180
# convert(2) ➞ 120
def convert(minutes):
    sec=minutes*60
    return sec
minutes=int(input("Enter the minutes:-"))
print(convert(minutes))