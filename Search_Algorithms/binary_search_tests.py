from binary_search import *
L = [2, 5, 6, 8, 9, 23, 45, 66, 78, 125, 456]
K = [3, 4, 10]

#%% Testing binary search
print(f"Testing binary_search() with list L={L}")
for i in range(len(L)): 
    print("Search for {0:3d} which is in L with index {1:3d} | binary_search(L,{0:3d}) ->  {2:}"\
        .format(L[i], L.index(L[i]), binary_search(L, L[i])))
for i in range(len(K)):
    print("Search for {0:3d} which is not in L | binary_search(L,{0:3d}) ->  {1:}"\
        .format(K[i], binary_search(L, K[i])))

#%% Testing recursive binary search
print(f"Testing binary_search_recursive() with list L={L}")
# for i in range(len(L)): 
#     print("Search for {0:3d} which is in L with index {1:3d} | binary_search_recursive(L,{0:3d},{3:},{4:}) ->  {2:}"\
#         .format(L[i], L.index(L[i]), binary_search(L, L[i]), 0, len(L)))
# for i in range(len(K)):
#     print("Search for {0:3d} which is not in L | binary_search_recursive(L,{0:3d},{2:},{3:}) ->  {1:}"\
#         .format(K[i], binary_search(L, K[i]), 0, len(L)))
for i in range(len(L)): 
    print("Search for {0:3d} which is in L with index {1:3d} | binary_search_recursive(L,{0:3d}) ->  {2:}"\
        .format(L[i], L.index(L[i]), binary_search(L, L[i])))
for i in range(len(K)):
    print("Search for {0:3d} which is not in L | binary_search_recursive(L,{0:3d}) ->  {1:}"\
        .format(K[i], binary_search(L, K[i])))
