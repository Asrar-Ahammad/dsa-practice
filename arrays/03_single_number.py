def single_number(nums) -> int:
    # count = {}
    #
    # for i in nums:
    #     if i not in count:
    #         count[i] = 1
    #     else:
    #         count[i]+=1
    #
    # for i in count:
    #     if count[i] == 1:
    #         return i

    result = 0
    for i in nums:
        result ^= i
    return result
print(single_number([4,1,2,1,2]))
print(single_number([1]))
print(single_number([2,2,1]))