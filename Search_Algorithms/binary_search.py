def binary_search(L, x):
    #We spot the mid element
    i=0
    j=len(L)
    while i<=j:
        mid = (i+j)//2
        mid_elem = L[mid]
        if x==mid_elem:
            return mid
        elif x>mid_elem:
            #go to next loop with list indexes: 
            i = mid+1
        else:
            #go to next loop with list indexes: 
            j = mid-1    
    #if we get out of while without finding target element, it's not present in L
    return None
    
def binary_search_recursive(L, x, i=0, j=-1):
    assert i>=0, j>=0
    if i <= j:
        mid = (i+j)//2
        mid_elem = L[mid]
        if  x == mid_elem:
            return mid
        elif x> mid_elem:
            # recursive call with left sublist - add mid to index to correct misaligned index
            return binary_search_recursive(L, i+1, j, x)
        else:
            # recursive call with right sublist
            return binary_search_recursive(L, i, j-1, x)
    # if first if is not confirmed and target elem is not found
    # then it's not present in L
    return None
    