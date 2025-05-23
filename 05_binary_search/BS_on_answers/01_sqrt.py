import math


def brute_force(num):
    ans = 1
    for i in range(1, num):
        ans = i * i
        if ans > num:
            return i - 1


def math_sqrt(num):
    return int(math.sqrt(num))


def square_root(num):
    low = 0
    high = num
    ans = 0

    while low <= high:
        mid = (low + high) // 2

        if mid * mid <= num:
            low = mid + 1
            ans = mid
        else:
            high = mid - 1

    return ans


num = 4
print(f'Square root of {num} is {square_root(num)}')
