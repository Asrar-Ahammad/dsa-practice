class isomorphic:
    def brute_force(self, s, t):
        s_di: dict[str, int] = {}
        t_di: dict[str, int] = {}

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

        s_arr: list[int] = []
        t_arr: list[int] = []

        for i in s_di:
            s_arr.append(s_di[i])

        for i in t_di:
            t_arr.append(t_di[i])

        s_count = {}
        t_count = {}

        for i in s_arr:
            if i not in s_count:
                s_count[i] = 1
            else:
                s_count[i] += 1

        for i in t_arr:
            if i not in t_count:
                t_count[i] = 1
            else:
                t_count[i] += 1

        for i in t_count:
            if i not in s_count or t_count[i] != s_count[i]:
                return False

        return True

    def optimal(self, s, t):
        mapST, mapTS = {}, {}

        for c1, c2 in zip(s, t):
            if (c1 in mapST and mapST[c1] != c2) or (c2 in mapTS and mapTS[c2] != c1):
                return False

            mapST[c1] = c2
            mapTS[c2] = c2

        return True


s = "foo"
t = "boo"
sol = isomorphic()
print(sol.brute_force(s, t))
print(sol.optimal(s, t))
