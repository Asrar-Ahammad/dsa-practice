# print(chr(65))
# print(ord('A'))

def pattern(n):
    start = 65
    for i in range(n):
        for j in range(i+1):
            print(chr(start+j), end=' ')
        print()
 
pattern(5)

