#%% Testing    
from linear_search import *
import time
import random 

n_elements = int(1e4)
L=[]
for i in range(n_elements):
    L.append(random.randint(1,500)) 
    
x = L[len(L)//2]
y = 501

print(f"Test functions on a random list with {n_elements}. Two testing cases: x={x} (belongs in list), y={y} (not in list)")


function_names = ["linear_search_for", "linear_search_for_no_range",
                  "linear_search_while1","linear_search_while2", 
                  "linear_search_while_sentinel"]

for fun_name in function_names:
    function = eval(fun_name) 
    start= time.time()
    fLx_res = function(L,x)
    fLx_time = time.time()-start

    start= time.time()
    fLy_res = function(L,y)
    fLy_time = time.time()-start
    
    print(f"{fun_name}(L, x): {fLx_res} (time elapsed: {fLx_time*1000} ms)")
    print(f"{fun_name}(L, y): {fLy_res} (time elapsed: {fLy_time*1000} ms)")