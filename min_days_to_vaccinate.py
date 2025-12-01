import math

# Function to calculate minimum days
def min_days_to_vaccinate(N, D, ages):
    risk = 0
    not_risk = 0

    # Counting at-risk and not-at-risk people
    for age in ages:
        if age >= 80 or age <= 9:
            risk += 1
        else:
            not_risk += 1

    # Calculate total days (ceil division)
    days = math.ceil(risk / D) + math.ceil(not_risk / D)
    return days

# Input section
T = int(input())
for _ in range(T):
    N, D = map(int, input().split())
    ages = list(map(int, input().split()))
    print(min_days_to_vaccinate(N, D, ages))
