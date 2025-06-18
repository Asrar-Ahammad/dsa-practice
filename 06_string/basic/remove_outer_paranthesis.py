def remove_outer_paranthesis(s):
    counter = 0
    ans = ""

    for i in range(len(s)):
        if s[i] == ")": counter -= 1
        if (counter != 0): ans += s[i]
        if s[i] == "(": counter += 1
    return ans


s = "(()())(()(()))"
print(remove_outer_paranthesis(s))
