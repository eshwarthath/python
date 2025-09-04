def bubble_sort(arr):
    for i in range(len(arr)-1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j+1]:
                final = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = final

n = int(input("Enter the number of elements to be stored in the list: "))

arr = []

for i in range(n):
    num = int(input(f"Enter number {i+1}: "))
    arr.append(num)

print(f"original list: ",arr)

bubble_sort(arr)

print(f"sorted list: ",arr)



