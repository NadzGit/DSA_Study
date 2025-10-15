import time
def sortTimeUsing(sortf,A):
    t = time.time()

    sortf(A)

    t = time.time()-t
    print("Sorted in ", t, "seconds")

def insertionSortC(A):
    B = A[:]

    for i in range (1, len(B)):
        j = i
        while j > 0 and B[j-1] > B[j]:
            B[j-1], B[j] = B[j], B[j-1]
            j -=1

        j += 1

    
    
    return B
