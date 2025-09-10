# ----- Alternatives (you can use any of these instead) -----
# 1) Bitwise (easy to understand)
def countBits(n):
    count = 0
    while n > 0:
        count += (n & 1)    # add 1 if last bit is 1
        n >>= 1             # shift right by 1 (drop last bit)
    return count
