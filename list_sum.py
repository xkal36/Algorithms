# Iterative solution:
def listsum(numList):
    theSum = 0
    for i in numList:
        theSum = theSum + i
    return theSum

# Recursive solution:
def listsum(numList):
   if len(numList) == 1:
        return numList[0]
   else:
        return numList[0] + listsum(numList[1:])


