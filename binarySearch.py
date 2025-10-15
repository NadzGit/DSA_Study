def findMid(i,j):
    mid = i + j //2

    return mid
def binarySearch(A, target): # binary search 
    i = 0
    j = len(A)-1  # upper and lower bound pointers
    pos = -1
    while i <= j: 
        mid = findMid(i, j) # use helper function to find midpoint
        if target == A[mid]:
                pos = mid
                return pos
        elif A[mid] < target: # if num at the midpoint is less than the target, shift the lower bound up to the midpoint (+1 because we already evaluated the midpoint != target num)
                i = mid + 1
        elif A[mid] > target: # if num at midpoint is greater than the tartget, shift the upper bound down to the midpoint (-1 because midpoint != target num)
                j = mid -1
           
    return pos
