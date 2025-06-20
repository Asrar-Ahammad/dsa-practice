def reverse_word(s):
    s = s.strip()
    s = s.split(" ")
    
    return (" ").join(s[::-1])


s = "the sky is blue"
print(reverse_word(s))
