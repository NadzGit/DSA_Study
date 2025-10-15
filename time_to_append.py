import time
import randomIntegerArray as ria

def appendTime(A,v):
    B = [None]* (len(A)+ 1)

    t = time.time()

    for i in range(len(B)-1):
        B[i] = A[i]

    
    B[-1] = v

    t = time.time()-t
    print(B)
    print("time taken to append: ", t)


tests = (ria.randomIntArray(i,100) for i in [0,10,100,1000,10000])
for A in tests:
    appendTime(A,42)
        
