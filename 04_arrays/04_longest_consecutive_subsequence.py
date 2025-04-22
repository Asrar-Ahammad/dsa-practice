# Method 1 O(nlogn)
# def longest_common_subsequence(nums):
#     nums.sort()
#     count = 1
#     max_length = 0
#
#     for i in range(len(nums)-1):
#         if nums[i+1]-nums[i] == 1:
#             count+=1
#         else:
#             max_length = max(max_length, count)
#             count = 1
#     max_length = max(max_length, count)
#     return max_length

# Method 2: O(n)
def longest_common_subsequence(nums):
    nums = set(nums)
    longest = 0

    for i in nums:
        if i-1 not in nums:
            length = 1
            
            while i+length in nums:
                length += 1
            longest = max(longest, length)

    return longest


print(longest_common_subsequence([0,3,7,2,5,8,4,6,0,1]))
print(longest_common_subsequence([100,4,200,1,3,2]))