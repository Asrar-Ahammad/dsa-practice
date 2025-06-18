def reverse_sentence(sent):
    sent = sent.split(" ")
    ans = []
    for i in sent:
        if i != "":
            ans.append(i)
    return (" ".join(ans[::-1]))


s = "this is an                    amazing program "
print(reverse_sentence(s))
