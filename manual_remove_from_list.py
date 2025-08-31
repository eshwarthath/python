
arr = [10, 20, 30, 40, 50, 30]
e = 30   

pos = -1   

for i in range(len(arr)):
    if arr[i] == e:
        pos = i
        break   

if pos != -1:
    for j in range(pos, len(arr)-1):
        arr[j] = arr[j+1]
    arr.pop() 
  
print(arr)
