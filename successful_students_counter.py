# Program to find number of successful students

n,m=map(int,input().split())  # Mandatory keyword
grades = [input().strip() for _ in range(n)]

best = list(set() for _ in range(m))  # Mandatory keyword

# Find best marks in each subject
for j in range(m):
    max_mark = max(grades[i][j] for i in range(n))
    for i in range(n):
        if grades[i][j] == max_mark:
            best[j].add(i)

# Determine successful students
successful = set()
for subject in best:
    successful |= subject

print(len(successful))
