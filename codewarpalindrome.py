# Write a function that checks if a given string (case insensitive) is a palindrome.
def is_palindrome(s):
    u=s.upper()
    i=0
    while i<len(u):
        a=u[::-1]
        i+=1
        if a==u:
            return True
        else:
            return False
print(is_palindrome("kodok"))
print(is_palindrome("Abba"))
print(is_palindrome("malam"))
print(is_palindrome("aba"))
print(is_palindrome("a"))
print(is_palindrome("walter"))
print(is_palindrome("kasue"))