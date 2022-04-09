# Write a function to split a string and convert it into an array of words.\
# Examples (Input -> Output):
# * "Robin Singh" ==> ["Robin", "Singh"]
# * "I love arrays they are my favorite" ==>
#  ["I", "love", "arrays", "they", "are", "my", "favorite"]
def string_to_array(s):
    a=s.split()
    s=""
    l=[]
    i=0
    while i<len(a):
        l.append(a[i])
        i+=1
    print(l)
string_to_array("codewar")
string_to_array("i love you")
string_to_array("1 2 3")
string_to_array("")
















