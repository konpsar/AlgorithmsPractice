def find_min_for(L):
    min_idx = 0
    for i in range(1,len(L)):
        if L[i] < L[min_idx]: 
            min_idx = i
    return L[i]

def find_min_while(L):
    min_idx = 0
    i=1
    while i<len(L):
        if L[i] < L[min_idx]: 
            min_idx = i
        i+=1
    return L[i]
