def bubbleSort(arr):
    # code here
    size = len(arr)

    for i in range(size):
        swapped = False
        for j in range(size - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if swapped == False:
            break

    return arr

print(bubbleSort([90,34,12,45,46,2]))