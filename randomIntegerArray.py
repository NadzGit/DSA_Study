import random

def randomIntArray(s,n):
    A = [None]*s
    for i in range(s):
        A[i] = random.randint(0,n)
    
    print(A)
    return A
    
