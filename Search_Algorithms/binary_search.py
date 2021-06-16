L=[2, 5, 6, 8, 9, 23, 45, 66, 78, 125, 456]

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
            print("indexes", i,j)
        elif x<mid_elem:
            #go to next loop with list indexes: 
            j = mid-1    
            print("indexes", i,j)
    #if we get out of while without finding target element, it's not present in L
    return None
    
for i in range(len(L)):
    print(i, L[i], binary_search(L, L[i]))