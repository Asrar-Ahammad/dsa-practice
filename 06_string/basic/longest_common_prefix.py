def longest_prefix(strs):
    res = ""
    for i in range(len(strs[0])):
        for s in strs:
            if i == len(s) or strs[0][i] != s[i]:
                return res
        res += strs[0][i]


strs = ["flowers", "flow", "fly", "flight"]
print(longest_prefix(strs))
