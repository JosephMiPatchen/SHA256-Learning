def evol_nums_prime(A, B, C, n, x=0):
    """
    Given:
      - A = buff[n-3]
      - B = buff[n-2]
      - C = buff[n-1]
      - n = buffer length
      - x = chosen value for the first seed element
    Returns a tuple: (c, seed=[x, y])
    """
    # 1) c = B - C
    c = B - C
    
    # 2) (x + y + c) = B / 2^(n-3)
    #    => (x + y) = (B / 2^(n-3)) - c
    x_plus_y = (B // (2**(n-3))) - c
    
    # 3) pick x, solve for y
    y = x_plus_y - x
    
    return c, [x, y]
