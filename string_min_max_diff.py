t = int(input())
for _ in range(t):
    s1=str(input())
    s2=str(input())
    min_diff = 0
    max_diff = 0
    for i in range(len(s1)):
        if s1[i] == '?' or s2[i] == '?':
            max_diff += 1
        elif s1[i] != s2[i]:
            min_diff += 1
            max_diff += 1
    print(min_diff, max_diff)
