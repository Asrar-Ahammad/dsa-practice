def pattern(n):

    for i in range(n):
        # Space
        for j in range(n-i-1):
            print(" ",end='')

        # Character
        break_point = (2*i+1)//2
        start=65
        for j in range(1,(2*i)+2):
            print(chr(start),end='')
            if j <= break_point: 
                start+=1
            else: 
                start-=1
        
        # Space
        for j in range(n-i-1):
            print(" ",end='')
        print()

pattern(5)