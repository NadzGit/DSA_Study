"""merge sort notes + code
it is a recursive function- once base case reached we call merge sort again(?)
divide and conquer algorithm
base case is when all sub-lists are of size 1
create second helper function called merge which takes all these sublists and slowly combines
them back into the original array they came from, but in order

in practice, instead of tackling all sub arrays in one go, we do it branch by branch
"""

"""
e.g
 mergeSort(1,3,6,24,6,25)
 mergeSort (1,3,6)  24,6,35
 mergeSort (1,3) 6
 mergeSort (1,3)
 merge(1 3) ^ back into this, in this case they are in the correct order.
 however, what you are doing is copying the values, in order, into the original array.
 so, if instead of 1,3 we had 3,1- we would copy 3, into A[1] and 1 into A[0]  
 https://www.youtube.com/watch?v=3j0SWDX4AtU 2:00
"""

"""
compare 1st element of first array to first element of 2nd array
if less than, move into original array and move pointer of this array to right
else:
move other element into original array and move second array pointer to the right
(I hope this makes sense in the future lol, if not watch brocode from 2:00 like I said)
"""


def mergeSort(A): 

    if len(A) <= 1:
        return A # first we want to continuously split, base case is len arrays = 1
    
    mid = len(A)//2 
    half1 = A[:mid] # split our arrays continuously in half
    half2 = A[mid:]

    mergeSort(half1)
    mergeSort(half2)
    merge(half1,half2,A)


def merge(half1,half2,A):
    i=0 #original array pointer
    j1= 0 #half1 pointer
    j2=0 # half2 pointer

    while j1< len(half1) and j2 < len(half2):
        if half1[j1] < half2[j2]:
            A[i] = half1[j1]
            j1 +=1
        else:
            A[i] = half2[j2]
            j2+=1

        i+=1
    
    # this part is to fill in the rest if there are any left over elements (say if its an uneven list)

    while j2 < len(half2):
        A[i] = half2[j2]
        i +=1
        j2 +=1
    
    while j1 < len(half1):
        A[i] = half1[j1]
        i +=1
        j1 +=1
    
A = [3,21,65,1,3,1,3,4,5,11,5,656,4,5,6,7,12]
mergeSort(A)
print(A)

