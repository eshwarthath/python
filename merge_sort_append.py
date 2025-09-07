def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        left_arr = arr[:mid]
        right_arr = arr[mid:]
        merge_sort(left_arr)
        merge_sort(right_arr)

        arr.clear()
        while len(left_arr)>0 and len(right_arr)>0:
            if left_arr[0]<=right_arr[0]:
                arr.append(left_arr[0])
                left_arr.pop(0)
            else:
                arr.append(right_arr[0])
                right_arr.pop(0)

        for i in left_arr:
            arr.append(i)
        for i in right_arr:
            arr.append(i)

n = int(input("Enter the number of elements to be stored in the list: "))

arr = []

for i in range(n):
    num = int(input(f"Enter number {i+1}: "))
    arr.append(num)

print(f"original list: ",arr)

merge_sort(arr)

print(f"sorted list: ",arr)


















