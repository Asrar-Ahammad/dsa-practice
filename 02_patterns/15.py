def pattern(n):
    start = 65

    for i in range(n,0,-1):
        for j in range(i):
            print(chr(start+j), end=' ')
        print()

pattern(5)