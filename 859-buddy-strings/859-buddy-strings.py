class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        diff = []
        for i in range(len(s)):
            if s[i] !=goal[i]:
                diff.append(i)
        if len(diff)>3:
            return False
        if len(diff)==2:
            if (s[diff[0]] == goal[diff[1]]) and (s[diff[1]]==goal[diff[0]]):
                return True
            else:
                return False
        if len(diff)==1:
            return False
        alpha = {}
        if len(diff)==0:
            for c in s:
                if c in alpha:
                    alpha[c]+=1
                else:
                    alpha[c]=1
            for c in alpha:
                if alpha[c] >=2:
                    return True
            return False
        