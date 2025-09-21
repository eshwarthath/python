
def merge_the_tools(s, k):
    n = len(s)

    for i in range(0, n, k):
        substring = s[i:i + k]
        result = ""

        for ch in substring:
            if ch not in result:
                result += ch
        print(result)


s = input().strip()
k = int(input().strip())
merge_the_tools(s, k)
