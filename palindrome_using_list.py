def palindrome(s):
    s_list = [char for char in s]
    still_equal = True
    i = 0
    len_s = len(s)
    while still_equal and len(s_list) > 1:
        first = s_list.pop(0)
        last = s_list.pop()
        if first != last:
            still_equal = False
    return still_equal




print palindrome('racecars')
