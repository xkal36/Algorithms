# Recursively converts an integer into any base:
def toStr(n,base):
    convertString = "0123456789ABCDEF"
    if n < base:
        return convertString[n]
    else:
        return toStr(n//base,base) + convertString[n%base]


# Produces the reverse of a string:
def reverse_string(s):
    if len(s) == 0:
        return s
    else:
        return s[-1] + reverse_string(s[:-1])


# Checks using recursion if a
# string is a palindrome or not
def is_palindrome(s, is_equal=True):
    if len(s) == 1:
        return is_equal
    else:
        if s[0] != s[-1]:
            return False
        else:
            return is_palindrome(s[1:-1])


print is_palindrome('kayak')
print reverse_string('adam')
