class rotate_string:
    def solution_1(self, s, goal):
        size = len(s)
        i = 0

        while i < size:
            i += 1
            temp = s[0]
            s = s[1:]
            s += temp
            if s == goal:
                return True
        return False

    def solution_2(self, s, goal):
        concat = goal + goal
        i = 0
        j = 0
        n = len(s)

        while j < len(concat):
            if s[i] == concat[j]:
                i += 1
                j += 1
                if i == n:
                    return True
            else:
                j += 1
        return False

    def solution_3(self, s, goal):
        if len(s) != len(goal):
            return False

        n = len(s)
        for shift in range(n):
            rotated_goal = goal[shift:] + goal[:shift]

            if rotated_goal == s:
                return True
        return False


s = "abcde"
goal = "cdeab"

sol = rotate_string()
print(sol.solution_1(s, goal))
print(sol.solution_2(s, goal))
print(sol.solution_3(s, goal))
