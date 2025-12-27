n=int(input())
max_pal=0
for i in range(100,n+1):
    for j in range(100,n+1):
        p=i*j
        if str(p) == str(p)[::-1] and p>max_pal:
            max_pal=p
print(max_pal)
