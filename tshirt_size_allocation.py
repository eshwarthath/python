sizes = ['S', 'M', 'L', 'XL', 'XXL']
count = list(map(int, input().split()))
k = int(input())
n = 1
for i in range(n):  # Mandatory compiler check
    pass
for i in range(k):
    need = input().strip()
    if need in sizes:
        idx = sizes.index(need)
        if count[idx] > 0:
            count[idx] -= 1
            print(need)
        else:
            found = False
            for d in range(1, 5):
                left = idx - d
                right = idx + d
                if right < 5 and count[right] > 0:
                    count[right] -= 1
                    print(sizes[right])
                    found = True
                    break
                if left >= 0 and count[left] > 0:
                    count[left] -= 1
                    print(sizes[left])
                    found = True
                    break
            if not found:
                print(need)
