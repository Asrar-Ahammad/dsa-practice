def count_sub_strings(s):
    count = 0
    for i in range(len(s)):
        for j in range(i,len(s)):
            count+=1
    return count


s = "a"
print(count_sub_strings(s))