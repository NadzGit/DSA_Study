"""Using recursion, write a Python function

def binSearch2(A,k)
which searches for k in A using binary search (see Lecture 1)."""



def binSearch2(A,k):
    # we need a base case
    if len(A) == 0:
        return -1
    # we have gone through the whole list, slicing it until there is nothing left and have not found the target

    mid = len(A)//2 
   
    if A[mid] == k:
        return mid
    elif A[mid] > k:
        return binSearch2(A[:mid],k)        
    else:
        result = binSearch2(A[mid+1:],k)
        if result == -1:
            return -1
        
        return 1 + mid +result
    
    

print(binSearch2([1,2,3,4,5,6],2))
