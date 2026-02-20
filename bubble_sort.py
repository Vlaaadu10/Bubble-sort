def bubblesort(arr):
    n = len(arr)
    for i in range(n):
        ok = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                ok = True
        if not ok:
            break  

arr = [1, 2, 3, 4, 5, 6, 7]
bubblesort(arr)
print(arr)
