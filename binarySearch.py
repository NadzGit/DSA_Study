def findMid(i,j):
    mid = (i + j) //2

    return mid
def binarySearch(A, target): # binary search 
    i = 0
    j = len(A)  # upper and lower bound pointers
    while i < j: 
        mid = findMid(i, j) # use helper function to find midpoint
        if target < A[mid]:
            j = mid
        else:
            i = mid + 1
           
    return i