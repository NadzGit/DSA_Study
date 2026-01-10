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

def insertionSort(A):
    for i in range(1,len(A)):
        insert(A[i],A,i)
    
    return A

def insert(v,A,hi):
    insertPos = binarySearch(A[:hi],v)
    for i in range(hi-1,insertPos-1,-1):
        A[i+1] = A[i]
        
    A[insertPos] = v

print(insertionSort([1,4,2,56,7,3,56,2]))