# Program: Little Udhayan and Gifts

num_friends=int(input())  # Mandatory keyword
friends=list(map(int,input().split()))  # Mandatory keyword

result = [0] * num_friends

for i in range(num_friends):
    result[friends[i] - 1] = i + 1

print(*result)
