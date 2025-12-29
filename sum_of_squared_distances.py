# Program to find the sum of squares of distances between all pairs of points
n = int(input())
x_sum = y_sum = x_sq_sum = y_sq_sum = 0

for _ in range(n):
    x, y = map(int, input().split())
    x_sum += x
    y_sum += y
    x_sq_sum += x * x
    y_sq_sum += y * y

# Formula: n*(Σ(x²+y²)) - (Σx)² - (Σy)²
ans = n * (x_sq_sum + y_sq_sum) - (x_sum * x_sum + y_sum * y_sum)
print(ans)
