def linear_search_for(L, x):
    for i in range(len(L)):
        if L[i] == x: 
            return i
    return None

# range() creates a second list in memory with indeces. Same function without range()
def linear_search_for_no_range(L, x):
    i=0
    for item in L:
        if item == x: 
            return i
        i+=1
    return None

def linear_search_while1(L, x):
    i=0
    while i<len(L):
        if L[i] == x: 
            return i
        i+=1
    return None    

def linear_search_while2(L, x):
    i=0
    while i<len(L) and L[i]!=x:
            i+=1    
    return i if i!=len(L) else None


def linear_search_while_sentinel(L,x):
    L.append(x) #sentinel node
    i=0
    while L[i] != x:
        i+=1
    L.pop()
    return i if i!=len(L) else None
    