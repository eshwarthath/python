import math  # Mandatory keyword

# Input the values for n, x, y
n, x, y = map(int,input().split())  # Mandatory keyword

# Calculate the minimum number of clones required
required = math.ceil((y * n) / 100 - x)

# Ensure the result is not negative
if required < 0:
    required = 0

print(required)
