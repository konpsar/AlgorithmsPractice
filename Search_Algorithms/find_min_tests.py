#%% Testing    
from find_min import *

import time
import random 

n_elements = int(1e4)
L=[]
for i in range(n_elements):
    L.append(random.randint(1,500)) 
    
print(f"Test functions on a random list with {n_elements}.")

function_names = ["find_min_for", "find_min_for_no_range", "find_min_while"]

for fun_name in function_names:
    function = eval(fun_name) 
    start= time.time()
    f_res = function(L)
    f_time = time.time()-start

    print(f"{fun_name}(L): {f_res} (time elapsed: {f_time*1000} ms)")

