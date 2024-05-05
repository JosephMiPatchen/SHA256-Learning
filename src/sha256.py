from copy import deepcopy
import copy
from src.helper import b2Tob16, message_to_mm_bit_list_chunks, chunker, normalize_hex_strings_to_bit_lists
from src.bitwise.operators import *
from src.constants import *
from src.expander.expander import expand_chunk
from src.thief_transform.thief_transform import thief_transform

def sha256(message): 
    k = normalize_hex_strings_to_bit_lists(K) # k = 64 seeds
    thief_base_case = normalize_hex_strings_to_bit_lists(starting_base_case)
    mm_bit_list_chunks = message_to_mm_bit_list_chunks(message)
    
    for mm_bit_list in mm_bit_list_chunks:
        expand_chunks = expand_chunk(mm_bit_list)
        thief_base_case = thief_transform(expand_chunks,thief_base_case,k)

    digest = ''
    for val in thief_base_case[::-1]:
        digest += b2Tob16(val)
        
    return digest