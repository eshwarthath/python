# Program to find determinant of a 2x2 matrix

# Reading the first row elements
a, b = map(int, input().split())

# Reading the second row elements
c, d = map(int, input().split())

# Calculating determinant (ad - bc)
det = (a * d) - (b * c)

# Printing the determinant value
print(det)
