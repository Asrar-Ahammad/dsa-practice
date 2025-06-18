def number_of_days(arr, mid):
    count = 1
    load = 0
    n = len(arr)

    for i in range(n):
        if load > mid:
            count += 1
            load = arr[i]
        else:
            load += arr[i]
    return count


def min_capacity(nums, days):
    low = max(nums)
    high = sum(nums)
    count = 0

    while low <= high:

        mid = (low + high) // 2
        # print(low, high, mid)
        count = number_of_days(nums, mid)

        if count <= days:
            high = mid - 1
        else:
            low = mid + 1

    return mid


nums = [5, 4, 5, 2, 3, 4, 5, 6]
days = 5
print(min_capacity(nums, days))
