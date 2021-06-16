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
        elif x<mid_elem:
            #go to next loop with list indexes: 
            j = mid-1    
    #if we get out of while without finding target element, it's not present in L
    return None
    