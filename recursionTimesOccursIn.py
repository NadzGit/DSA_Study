# Write a Python function
   
#     def timesOccursIn(k,A)
    
# which which takes an integer and an array of integers and returns the number of times the
# integer occurs in the array. You must use recursion and no loops for this question.

# For example, if its arguments are `5` and `[1,2,5,3,6,5,3,5,5,4]` the function should return `4`.

# _Hint:_ Suppose `A` is not empty. If the first element of `A` is in fact `k`, the number of times that `k`
# occurs in `A` is “1 + the number of times it occurs in `A[1:]`”. Otherwise, it is the same as the
# number of times it occurs in `A[1:]`. On the other hand, if `A` is the empty array `[]` then `k`
# occurs 0 times in it.


def timesOccursIn(k,A):
    if len(A) == 0:
        return 0 

    if A[0] == k:
        return 1+ timesOccursIn(k, A[1:])
    
    
    else: 
        return timesOccursIn(k,A[1:])
    

    
    

print(timesOccursIn(2, [1,3,5,2,2,4,52,2]))