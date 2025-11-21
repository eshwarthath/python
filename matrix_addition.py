r = int(input())
c = int(input())

a = []
for i in range(r):
    row = []
    for j in range(c):
        row.append(int(input()))
    a.append(row)

b = []
for i in range(r):
    row = []
    for j in range(c):
        row.append(int(input()))
    b.append(row)

for i in range(r):
    for j in range(c):
        print(a[i][j] + b[i][j], end=" ")
    print()
