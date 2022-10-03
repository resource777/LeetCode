class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        tmp = ''
        for i in digits:
            tmp+=str(i)
        tmp= int(tmp) +1
        ans = []
        for i in str(tmp):
            ans.append(int(i))
        return ans
            