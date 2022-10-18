class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dic = {}
        for n in nums:
            if n not in dic:
                dic[n]=1
            else:
                dic[n]+=1
        for i,times in dic.items():
            if times>len(nums)//2:
                return i

        