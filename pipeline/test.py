def isSorted(a):
    # b = a ( This doesn't work, as it is again the reference of a is assigned to b)
    # we need to do a shallow copy
    # b = a.copy()
    # a.sort()
    # return a == b
def isSorted(a):
    for i in range(len(a)-1, 1,-1):
        if a[i] < a[i-1]:
            return False
    return True


# a = [3,2,4,5,1]

a = [1,2,3,4,6]
print(isSorted(a))
# print(isSorted(a))
