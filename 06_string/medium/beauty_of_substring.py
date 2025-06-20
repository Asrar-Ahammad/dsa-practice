# def calculate_beauty(s):
#     di = {}
#     for i in s:
#         if i not in di:
#             di[i] = 1
#         else:
#             di[i]+=1
            
#     # freq = []
#     # for i in di:
#     #     freq.append(di[i])
    
#     # if max(freq) - min(freq) > 0:
#     #     return max(freq) - min(freq)
#     # else:
#     #     return 0

#     max_num = float('-inf')
#     min_num = float('inf')

#     for i in di.values():
#         max_num = max(i, max_num)
#         min_num = min(i, min_num)

#     return max_num-min_num

# def beauty_of_substring(s):
#     sum = 0

#     for i in range(len(s),-1,-1):
#         for j in range(i):
#             sum += calculate_beauty(s[j:i])

#     return sum


# def solution_2(s):
#     total_beauty = 0
#     n = len(s)

#     for i in range(n, -1, -1):
#         freq = {}
#         for j in range(i):
#             char = s[j]
#             if char not in freq:
#                 freq[char] = 1
#             else:
#                 freq[char]+=1
#             # freq[char] = freq.get(char,0)+1

#             max_num = float('-inf')
#             min_num = float('inf')
#             for count in freq.values():
#                 min_num = min(min_num, count)
#                 max_num = max(max_num, count)
            
#             total_beauty += (max_num - min_num)
    
#     return total_beauty

from concurrent.futures import ThreadPoolExecutor

def calculate_beauty(s, i):
    n = len(s)
    freq = [0]*26
    total = 0

    for j in range(i ,n):
        freq[ord(s[j]) - ord('a')] += 1
        max_fres = max(f for f in freq if f > 0)
        min_freq = min(f for f in freq if f > 0)
        total += (max_fres- min_freq)
    
    return total

def beauty_of_substring1(s):
    n = len(s)
    with ThreadPoolExecutor() as executor:
        results = list(executor.map(lambda i: calculate_beauty(s, i), range(n)))
        return sum(results)

s = "aabcbaa"*2000
print(beauty_of_substring1(s))