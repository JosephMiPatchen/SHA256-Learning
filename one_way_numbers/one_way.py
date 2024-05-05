from numpy import *

def evolution_nums(n=3,starting_state=[1312,321]):
    number_window_len = 5
    buff = starting_state + ([0] *  (n-1)) + ([0] * number_window_len)
    c = 2
    
    for i in range(2,2+n-1+number_window_len):
        val = buff[i-1] + buff[i-2]
        buff[i-1] = val + c
        buff[i] = val
    
    print(f"buff:{buff}")    
    print(f"set:{buff[-number_window_len:]}")
    
def evolution_nums_prime(nums):
    pass