class Solution:
    def isPalindrome(self, s: str) -> bool:
        st = ""
        tmp = s.lower()
        for t in tmp:
            if t in "abcdefghijklmnopqrstuvwxyz0123456789":
                st+=t
        for i in range(len(st)//2):
            if st[i] != st[len(st)-1-i]:
                return False
        return True