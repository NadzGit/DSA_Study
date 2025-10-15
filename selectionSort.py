def selectionSort(A):
    for i in range(len(A)):
        imin = findMin(A,i)
        swap(A, i, imin)


def findMin(A,i):
    imin = i
    for j in range(i + 1, len(A)):
        if A[j] < A[imin]:
            imin = j
    return imin

def swap (A, i ,j):
    A[i], A[j] = A[j], A[i]
