"""Using recursion, write a Python function

def printArray(A)
that prints the elements of A, in order, one element per line.

Now, using recursion, write a Python function

def printArrayRev(A)
that prints the elements of A, in reversed order, one element per line."""

def printArray(A):
    if len(A) == 0:
        return

    print(A[0])
    printArray(A[1:])
    

def printArrayRev(A):
    if len(A) == 0:
        return

    print(A[-1])
    printArrayRev(A[:-1]) 

# printArray([1,4,22,452,2])
printArrayRev([1,4,22,452,2])

