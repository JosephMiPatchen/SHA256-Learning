'''def xor(i, j): return if_(i, not_(j), j)

def zexor(i, j): return [xor(ia, ja) for ia, ja in zip(i, j)]

def xorxor(i, j, l): return xor(i, xor(j, l))

def zxx(i:list[int], j:list[int], l:list[int]): return [xorxor(ia, ja, la) for ia, ja, la, in zip(i, j, l)]'''