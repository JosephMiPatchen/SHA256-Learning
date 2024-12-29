from numpy import *

def evol_nums(n=8, seed=[3,1],c=2):
    buff = seed + ([0] * (n - 2))
    
    for i in range(2,len(buff)):
        val = buff[i-1] + buff[i-2]
        buff[i] = val
        buff[i-1] = buff[i] + c
 
    return buff