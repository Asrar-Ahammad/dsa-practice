def max_consecutive_ones(nums):
    curr = 0
    n_max = 0
    for i in nums:
        if i == 1:
            curr += 1
        else:
            n_max = max(curr,n_max)
            curr = 0
    n_max = max(curr,n_max)
    return n_max

print(max_consecutive_ones([1,1,0,1,1,1]))
print(max_consecutive_ones([1,0,1,1,0,1]))