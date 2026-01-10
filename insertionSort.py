def insertionSort(A):
    for i in range(1,len(A)): # why do we start at 1? we start at one because we are constantly comparing v with the value before v:
        # at the beginning of this loop it means we must compare v (A[1]) to A[0]. If the loop started at 0, we would be comparing the beginning
        # to the end which makes no logical sense.
        insert(A[i],A,i)

def insert(v,A,hi):
    for i in range(hi-1,-1,-1): # remember loops are non-inclusive: it will never hit A[-1]. The reason we go to -1 is because
        # we want to be able to traverse backwards to (and including) 0.
        if v >= A[i]: # check if the number you want to insert (v) is greater than or equal to the element directly to its left
            A[i+1] = v # if it is greater, then store v directly to the right of the element we are comparing v to.
            return
        
        A[i+1] = A[i] # if v is smaller than the element to its left, then shift that element to the right to make space for v later down the line
    A[0] = v # if we get through the whole process and v is smaller than all the elements to its left and therefore the loop has not returned early at all,
    # then v must be the smallest value so far, and we must place it at the beginning.

    
