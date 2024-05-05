def isTrue(x): return x == 1

def if_(i, y, z): return y if isTrue(i) else z

def and_(i, j): return if_(i, j, 0)

def zand(i, j): return [and_(ia, ja) for ia, ja in zip(i,j)] 

def not_(i): return if_(i, 0, 1)

def not_map(i): return [not_(x) for x in i]

def xor(i, j): return if_(i, not_(j), j)

def zexor(i, j): return [xor(ia, ja) for ia, ja in zip(i, j)]

def xorxor(i, j, l): return xor(i, xor(j, l))

def zxx(i:list[int], j:list[int], l:list[int]): return [xorxor(ia, ja, la) for ia, ja, la, in zip(i, j, l)]

# return the value that appears the most between i , j , k
def majority_value(i,j,k):
  d = {}
  
  for ele in [i,j,k]:
    if ele in d:
      return ele
    else:
      d[ele] = None
      
  return i

# circular right shift on bit list by n positions
# example:
# input: [1,0,1],1
# output: [1,1,0]
def crs(x, n): return x[-n:] + x[:-n]

# logical right shift on bit list by n positions
# example:
# input: [1,0,1],1
# output: [0,1,0]
def lrs(x, n): return n * [0] + x[:-n]

def add(i, j):
  length = len(i)
  sums = list(range(length))
  c = 0
  for x in range(length-1,-1,-1):
    sums[x] = xorxor(i[x], j[x], c)
    c = majority_value(i[x], j[x], c)
  return sums