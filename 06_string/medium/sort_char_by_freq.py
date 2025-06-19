def frequencySort(s):
    s_di = {}
    ans = ''
    for i in s:
        if i not in s_di:
            s_di[i] = 1
        else:
            s_di[i] += 1
    sorted_di = dict(sorted(s_di.items(), key=lambda item: item[1], reverse=True))

    for c, i in sorted_di.items():
        ans += c * i
    return ans


s = "Aabb"
print(frequencySort(s))
