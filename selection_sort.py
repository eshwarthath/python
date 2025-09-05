def selection_sort(arr):

    for i in range(5):
        min_index = i
        for j in range(i, 6):
            if arr[j] < arr[min_index]:
                min_index = j


        temp = arr[i]
        arr[i] = arr[min_index]
        arr[min_index] = temp


arr = [5, 3, 8, 6, 7, 2]

selection_sort(arr)

print(arr)
