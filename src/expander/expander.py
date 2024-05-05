from src.helper import b2Tob16, message_to_mm_bit_list_chunks, chunker, normalize_hex_strings_to_bit_lists
from src.bitwise.operators import *
from src.constants import *

def expand_chunk(chunk):    
    sub_chunks = chunker(chunk, 32)
    
    # cop 1 - expander 
    memo = {}
    def new_sub_chunk(i,memo):
        # base case
        if i in memo:
            return memo[i]
        if i < 16:
            return sub_chunks[i]
        
        # rec rel
        g_x = zxx(
            crs(new_sub_chunk(i-15,memo), 7), 
            crs(new_sub_chunk(i-15,memo), 18), 
            lrs(new_sub_chunk(i-15,memo), 3))
        h_x = zxx(
            crs(new_sub_chunk(i-2,memo), 17), 
            crs(new_sub_chunk(i-2,memo), 19), 
            lrs(new_sub_chunk(i-2,memo), 10))
        new_chunk = \
        add(
            add(
                add(
                    new_sub_chunk(i-16,memo),g_x
                ),new_sub_chunk(i-7,memo)
            ),h_x
        )
        
        memo[i] = new_chunk
        
        return memo[i] 
    
    # add expanded chunks
    for x in range(16, 64):
        sub_chunks.append(new_sub_chunk(x,memo))
            
    return sub_chunks