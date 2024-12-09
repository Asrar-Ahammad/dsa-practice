def selectionSort(arr):
        # code here
        size = len(arr)

        for i in range(size):
            for j in range(i + 1, size):
                if arr[i] > arr[j]:
                    arr[i], arr[j] = arr[j], arr[i]
        return arr

print(selectionSort([90,34,12,45,46,2]))