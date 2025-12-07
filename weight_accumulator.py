w=int(input())
l = list(map(int,input().split()))

l.sort(reverse=True)
total = 0
count = 0

for i in range(len(l)):
    if total >= w:
        break
    total += l[i]
    count += 1

if total >= w:
    print(count)
else:
    print(-1)
