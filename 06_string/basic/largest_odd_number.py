def largest_odd(s: str):
    if int(s[-1]) % 2 == 1 and int(s[0]) == 0:
        return s[1:]
    if int(s[-1]) % 2 == 1:
        return s

    for i in range(len(s) - 1, -1, -1):
        if int(s[i]) % 2 != 0:
            return s[:i + 1]
    return None


s = "1234"
print(largest_odd(s))
