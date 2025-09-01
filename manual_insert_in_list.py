
arr = [10, 20, 30, 40, 50]
i = 2   
e = 99  

arr.append(0)

for j in range(len(arr)-1, i, -1):
    arr[j] = arr[j-1]

arr[i] = e

print(arr)
