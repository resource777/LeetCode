class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        leng=200
        for s in strs:
            if leng> len(s):
                leng = len(s)
        ans=''
        for i in range(leng):
            comp = strs[0][i]
            for j in range(1,len(strs)):
                if strs[j][i] != comp:
                    return ans
            ans+=comp
        return ans