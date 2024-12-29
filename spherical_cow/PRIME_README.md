# Recovering Evol Numbers Parameters from the Last Three Elements

This guide explains how to reverse-engineer valid parameters—a constant `c` and a seed pair `[x, y]`—from just the **last three elements** of an Evol Numbers buffer, given the buffer length `n`. This method reconstructs a valid triple `(c, x, y)` that reproduces the same final three elements but is not necessarily unique.

---

## 1. Key Background and Formulas

From the Evol Numbers algorithm, the following relationships hold for the last three elements of the buffer:

1. `buff[n-3] = 2**(n-4) * (x + y + c)`
2. `buff[n-2] = 2**(n-3) * (x + y + c)`
3. `buff[n-1] = 2**(n-3) * (x + y + c) - c`

Let’s denote these elements as:
- `A = buff[n-3]`
- `B = buff[n-2]`
- `C = buff[n-1]`

Using these values, we derive the following relationships:

1. `B = 2 * A`
2. `C = B - c`
3. `B = 2**(n-3) * (x + y + c)`

These relationships allow us to recover `c` and `(x + y + c)`, which in turn leads to `(x + y)`.

---

## 2. Algorithm for Recovery

### Step 1: Solve for `c`
From the relationship `C = B - c`:
```
c = B - C
```

### Step 2: Solve for `x + y + c`
From the relationship `B = 2**(n-3) * (x + y + c)`:
```
x + y + c = B / 2**(n-3)
```

### Step 3: Solve for `x + y`
Given `c` from Step 1:
```
x + y = (B / 2**(n-3)) - c
```

### Step 4: Choose `x` and Solve for `y`
Since `x + y` is known, you can pick any integer `x` and compute `y`:
```
y = (B / 2**(n-3)) - c - x
```

---

## 3. Example Calculation

Suppose the last three elements of the buffer are:
```
A = 192, B = 384, C = 382, n = 8
```

### Step-by-Step Solution

1. **Calculate `c`:**
```
c = B - C = 384 - 382 = 2
```

2. **Calculate `x + y + c`:**
```
x + y + c = B / 2**(n-3) = 384 / 2**5 = 384 / 32 = 12
```

3. **Calculate `x + y`:**
```
x + y = 12 - c = 12 - 2 = 10
```

4. **Pick `x` and Calculate `y`:**
For `x = 3`:
```
y = 10 - x = 10 - 3 = 7
```

Thus, a valid solution is:
- `c = 2`
- `seed = [3, 7]`

---

## 4. Python Implementation

Below is a Python script that automates the recovery process and verifies the solution:

```python
# Function to recover c and seed from last three elements
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
    
    # 2) (x + y + c) = B / 2**(n-3)
    x_plus_y = (B / (2**(n-3))) - c
    
    # 3) Pick x, solve for y
    y = x_plus_y - x
    
    return c, [x, y]

# Evol Numbers Generator
def evol_nums(n, seed, c):
    """Standard Evol algorithm from the README."""
    buff = list(seed) + [0] * (n - len(seed))
    for i in range(2, n):
        buff[i] = buff[i-1] + buff[i-2]
        buff[i-1] = buff[i] + c
    return buff

# Example Usage
A, B, C, n = 192, 384, 382, 8
c, seed = evol_nums_prime(A, B, C, n, x=3)
print("Reconstructed solution:")
print("  c   =", c)
print("  seed =", seed)

# Verify by running Evol forward
buff_check = evol_nums(n, seed, c)
print("\nVerification buffer =", buff_check)
print("Last three elements =", buff_check[-3:])
```

---

## 5. Example Test Cases

### Test Case 1
**Parameters:**
- `c = 2`
- `n = 9`
- `seed = [0, 4]`

**Result:**
```
[0, 6, 12, 24, 48, 96, 192, 384, 382]
```

### Test Case 2
**Parameters:**
- `c = 2`
- `n = 9`
- `seed = [1, 3]`

**Result:**
```
[1, 6, 12, 24, 48, 96, 192, 384, 382]
```

### Test Case 3
**Parameters:**
- `c = 2`
- `n = 9`
- `seed = [2, 2]`

**Result:**
```
[2, 6, 12, 24, 48, 96, 192, 384, 382]
```

### Test Case 4
**Parameters:**
- `c = 2`
- `n = 9`
- `seed = [-8, 12]`

**Result:**
```
[-8, 6, 12, 24, 48, 96, 192, 384, 382]
```

---

## 6. Final Takeaways

- You can recover a valid `c` and seed `[x, y]` from the **last three elements** and `n`.
- The solution is **not unique**: there are infinitely many valid seeds for a fixed `c`.
- This approach demonstrates the structured growth pattern in Evol Numbers, making parameter recovery straightforward and verifiable.

