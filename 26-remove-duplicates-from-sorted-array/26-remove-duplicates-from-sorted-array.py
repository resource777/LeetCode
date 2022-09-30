class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        leng = len(nums)
        tmp = sorted(list(set(nums)))
        ans = len(tmp)
        
        for i in range(len(tmp)):
            nums[i]=tmp[i]
        return ans
        
        