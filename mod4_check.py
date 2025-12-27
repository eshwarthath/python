# Program to increment or decrement a number based on divisibility by 4

# Read the input integer
A = int(input())

# Check divisibility and update accordingly
if A % 4 == 0:
    A = A + 1
else:
    A = A - 1

# Print the final result
print(A)
