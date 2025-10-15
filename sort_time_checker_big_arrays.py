import randomIntegerArray as ria
import sort_time as st
import insertionSort as ins
import selectionSort as sel


tests = (ria.randomIntArray(i,100) for i in [100000])
for A in tests:
    st.sortTimeUsing(sel.selectionSort,A)
    st.sortTimeUsing(ins.insertionSortC, A)






