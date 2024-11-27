def pattern(n):
    start=65

    for i in range(n):
        for j in range(i+1):
            print(chr(start),end=' ')
        start+=1
        print()

pattern(5)