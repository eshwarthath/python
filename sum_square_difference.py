# Program to find the difference between the sum of the squares and the square of the sum

n = int(input())
numbers = []

for i in range(1, n + 1):
    numbers.append(i)

sum_of_squares = sum([x ** 2 for x in numbers])
square_of_sum = sum(numbers) ** 2

print(square_of_sum - sum_of_squares)
