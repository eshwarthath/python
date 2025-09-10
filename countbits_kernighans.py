# 2) Brian Kernighan's method (fast when number has few 1s)
def countBits(n):
    count = 0
    while n:
        n &= (n - 1)   # removes the lowest set bit
        count += 1
    return count
