def missing_number(nums):
    n = len(nums)
    n_sum = (n*(n+1))//2
    total = sum(nums)
    return n_sum - total

print(missing_number([1,2,0]))