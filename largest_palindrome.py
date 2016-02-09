def all_substrings(input_string):
    length = len(input_string)
    return filter(lambda x: len(x) > 1, 
        [input_string[i:j+1] for i in xrange(length) for j in xrange(i,length)])



def is_palindrome1(s):
    s_list = [char for char in s]
    still_equal = True
    while still_equal and len(s_list) > 1:
        first = s_list.pop(0)
        last = s_list.pop()
        if first != last:
            still_equal = False
    return still_equal


def is_palindrome2(s):
    if len(s) < 2:
        return True
    else:
        if s[0] == s[-1]:
            return is_palindrome2(s[1:-1])
        else:
            return False      
    
    
    

def largest_palindrome(s):
    all_subs = all_substrings(s)
    pals = filter(lambda sub_st: is_palindrome2(sub_st), all_subs)
    return max(pals, key=len)

print largest_palindrome('Hello this is a racecar')
