# insertion sort
# the correct way to go about this is traversing an array BACKWARDS.
# compare value (v) you want to insert with the already sorted elements on the LEFT
# shift any elements that are larger than v to the RIGHT
# by traversing backwards, we are able to avoid any overwriting
# how? see below.

# (we skipped the first couple sorts)
# 1,3,65|21,3,1 <-- here, 21 is less than 65.
# 1,3,65,65,|3,1 <-- we shift 65 to the right. it may appear that we have lost the value of 21, but it is saved in a variable passed to the function.
# 1,3,21,65,|3,1 <-- 21 >= 3, so this is where we place 21.

def insertionSort(A):
    for i in range(1,len(A)):
        insert(A[i],A,i)

def insert(v, A, hi):
    for i in range (hi-1,-1,-1):
        if v >= A[i]:
            A[i+1] = v
            return
        A[i+1] = A[i]
    A[0] = v

A = [1,3,3,7,5]  
insertionSort(A)
print(A)