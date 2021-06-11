#linear search for the minimum element in a list starting from a specific index
def find_min_from(L, startFrom):
    min_idx = startFrom
    for i in range(startFrom+1, len(L)):
        if L[i]<L[min_idx]:
            min_idx = i
    return min_idx 

# Selection sort implementation
def selection_sort(L):
    for i in range(len(L)):
        min_idx = find_min_from(L, i)
        L[i], L[min_idx] = L[min_idx], L[i]
        
        
# pop current element and put it in the appropriate position
def insert_pop(L, idx):
    temp = L.pop(idx)
    i=idx-1
    while i>0 and L[i-1] > L[i]:
        i-=1
    L.insert(temp, i)
    
    
def insertion_sort(L):
    for i in range(1, len(L)):
        insert_pop(L,i)
