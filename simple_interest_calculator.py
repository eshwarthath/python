import math

principal = float(input())
rate = float(input())
time = float(input())

simple_interest = (principal * rate * time) / 100

simple_interest_floor = math.floor(simple_interest)

print(simple_interest_floor)
