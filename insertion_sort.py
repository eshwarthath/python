def insertion_sort(arr):

    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j>=0 and arr[j] > key:
            arr[j+1] = arr[j]
            j = j-1
        arr[j+1] = key

n = int(input("Enter the number of elements to be stored in the list: "))

arr = []

for i in range(n):
    num = int(input(f"Enter number {i+1}: "))
    arr.append(num)

print(f"original list: ",arr)

insertion_sort(arr)

print(f"sorted list: ",arr)

