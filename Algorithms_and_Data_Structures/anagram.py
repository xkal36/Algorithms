"""
We show three different 
solutions to the anagram detection
problem.

One string is an anagram of another if the second
is simply a rearrangement of the first.

The brute force approach would be to generate
all possible permutatiosn of one string and check
if each one is equal to the second string. This
would have a running time of n! so we do not
include it here.
"""

# O(n**2) running time:
def anagram_sol_1(s1, s2):
    """
    Checks to see that each character 
    in the first string occurs in the second. 
    Checking off a character is done 
    by replacing it with the value  None.
    """

    alist = list(s2)

    pos1 = 0
    stillOK = True

    while pos1 < len(s1) and stillOK:
        pos2 = 0
        found = False
        while pos2 < len(alist) and not found:
            if s1[pos1] == alist[pos2]:
                found = True
            else:
                pos2 = pos2 + 1

        if found:
            alist[pos2] = None
        else:
            stillOK = False

        pos1 = pos1 + 1

    return stillOK


# Same running time as underlying sorting algorithm used:
def anagram_solution_2(s1,s2):
    """
    Sorts each string alphabetically, 
    from a to z. If we end up with the same 
    string, then the original two strings are anagrams. 
    """

    alist1 = list(s1)
    alist2 = list(s2)

    alist1.sort()
    alist2.sort()

    pos = 0
    matches = True

    while pos < len(s1) and matches:
        if alist1[pos]==alist2[pos]:
            pos = pos + 1
        else:
            matches = False

    return matches


# O(n) running time:
def anagram_solution_3(s1,s2):
    c1 = [0] * 26
    c2 = [0] * 26

    for i in range(len(s1)):
        pos = ord(s1[i]) - ord('a')
        c1[pos] = c1[pos] + 1

    for i in range(len(s2)):
        pos = ord(s2[i]) - ord('a')
        c2[pos] = c2[pos] + 1

    j = 0
    stillOK = True
    while j < 26 and stillOK:
        if c1[j] == c2[j]:
            j = j + 1
        else:
            stillOK = False

    return stillOK
