"""Write a Python function

def multArray(A,k)
which takes an array A of integers and an integer k and changes A by multiplying each of its elements by k. You must 
use recursion and no loops for this question. For example, if it takes the array [5,12,31,7,25] and the integer 10, it 
changes the array so that it becomes [50,120,310,70,250].

Hint: The following “solution” will not work, as each recursive call creates a new copy of A so the original A is not changed.

def multAllNope(k,A):
    if A == []: return
    A[0] = A[0]*k
    return multAllNope(k,A[1:])        
Instead, the trick to do this is to define an auxiliary function multAllRec(k,A,i) which multiplies all elements of A[i:] by k.
 This function can then be defined with recursion."""


def multArray(A,k):
    multAllRec(k, A,0)
    return A

def multAllRec(k,A,i):
    if i >= len(A):
        return
    
    A[i] = A[i]*k
    multAllRec(k,A, i+1)

print(multArray([1,2,3,4,5], 11))