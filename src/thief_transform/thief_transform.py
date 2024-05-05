from src.bitwise.operators import *

def thief_transform(expand_chunks,base_case,k):
    # create tabulation table with base case
    tabu = base_case + [0] * 64
    
    # fill out table with thief algo recurrence relation
    for i in range(len(base_case), 64 + len(base_case)):
        # compute h_x 
        h_x_1 = zxx(crs(tabu[i-5], 6), 
                    crs(tabu[i-5], 11), 
                    crs(tabu[i-5], 25))
        h_x_2 = zexor(zand(tabu[i-5], tabu[i-6]), 
                    zand(
                    not_map(tabu[i-5]), tabu[i-7]))
        h_x = add(add(add(add(tabu[i-8], h_x_1), h_x_2), k[i-len(base_case)]), expand_chunks[i-len(base_case)])
        
        # compute g_x
        g_x_1 = zxx(crs(tabu[i-1], 2), 
                    crs(tabu[i-1], 13), 
                    crs(tabu[i-1], 22))
        g_x_2 = zxx(zand(tabu[i-1], tabu[i-2]), 
                    zand(tabu[i-1], tabu[i-3]), 
                    zand(tabu[i-2], tabu[i-3]))
        g_x = add(g_x_1, g_x_2)
        
        tabu[i-4] = add(tabu[i-4],h_x) # wow!!!!????
        tabu[i] = add(h_x,g_x)
    
    new_base_case = [add(bc_ele, tb_ele) for bc_ele, tb_ele in zip(base_case, tabu[-8:])]
    
    return new_base_case
