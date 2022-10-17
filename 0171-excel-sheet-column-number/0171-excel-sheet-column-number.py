class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        ans = 0
        slen = len(columnTitle)-1
        for i in range(len(columnTitle)):
            ans+=(ord(columnTitle[i])-ord('A')+1)*(26**slen)
            slen-=1
        return ans
        