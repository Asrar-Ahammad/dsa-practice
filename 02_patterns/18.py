def pattern(n):
    start = 65

    for i in range(n, start-1,-1):
        for j in range(i, n+1):
            print(chr(j), end=' ')
        print()

pattern(70)

# 5
# 4 5
# 3 4 5
# 2 3 4 5
# 1 2 3 4 5