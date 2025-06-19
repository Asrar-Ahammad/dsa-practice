def myAtio(s):
    i = 0
    n = len(s)

    while i<n and s[i]==" ":
        i+=1
    
    sign = 1
    sign_check = False
    while i<n and(s[i]=="-" or s[i]=="+"):
        sign = -1 if s[i]=="-" else 1
        if sign:
            return 0
        i+=1
        sign = True

    result = 0
    while i<n and s[i].isdigit():
        result = (result*10)+ int(s[i])

        if result*sign > (2**31)-1:
            return (2**31)-1
        if result*sign < (-2**31):
            return -2**31
        
        i+=1
    return sign*result


s = "+-12"
print(myAtio(s))
print(-2**31)