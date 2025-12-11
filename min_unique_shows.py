try:
    t = int(input())
    for _ in range(t):
        n, k, d = map(int, input().split())
        shows = list(map(int, input().split()))
        ans = k
        for i in range(n - d + 1):
            ans = min(ans, len(set(shows[i:i + d])))
        print(ans)
except:
    pass
