#21. Anagrams
# Two strings are anagrams if you can make one from the other by rearranging
# the letters.Write a function named is_anagram that takes two strings as its
# parameters. Your function should return True if the strings are anagrams,
# and False otherwise.
# For example, the call is_anagram("typhoon", "opython") should 
# return True while the call is_anagram("Alice", "Bob") should return False.
def anagram(s1, s2):
    i=0
    while i<len(s1):
        if s1[i] in s2:
            return True
        else:
            return False
        i+=1
s1=input("Enter the string:-")
s2=input("Enter the string:-")
print(anagram(s1,s2))
