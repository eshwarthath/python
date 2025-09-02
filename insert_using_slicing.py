def insert_with_slice(arr, i, e):
    if i < 0:
        i = 0
    if i > len(arr):
        i = len(arr)
    return arr[:i] + [e] + arr[i:]

print(insert_with_slice([10, 20, 30, 40, 50], 2, 99))




