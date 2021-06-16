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
    
L = [2, 5, 6, 8, 9, 23, 45, 66, 78, 125, 456]
K = [3, 4, 10]
print(L)
for i in range(len(L)): 
    print("Search for {0:3d} which is in L with index {1:3d} | binary_search(L,{0:3d}) ->  {2:}"\
        .format(L[i], L.index(L[i]), binary_search(L, L[i])))
for i in range(len(K)):
    print("Search for {0:3d} which is not in L | binary_search(L,{0:3d}) ->  {1:}"\
        .format(K[i], binary_search(L, K[i])))
