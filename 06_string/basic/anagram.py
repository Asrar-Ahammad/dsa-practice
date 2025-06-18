class anagram:
    def solution_1(self, s, t):
        if len(s) != len(t):
            return False

        s_di, t_di = {}, {}
        for i in s:
            if i not in s_di:
                s_di[i] = 1
            else:
                s_di[i] += 1

        for i in t:
            if i not in t_di:
                t_di[i] = 1
            else:
                t_di[i] += 1

        for i in s_di:
            if (i not in t_di) or s_di[i] != t_di[i]:
                return False

        return True

    def solution_2(self, s, t):
        s = list(s)
        t = list(t)
        s.sort()
        t.sort()
        return s == t


s = "CAT"
t = "ACT"
sol = anagram()
print(sol.solution_1(s, t))
print(sol.solution_2(s, t))
