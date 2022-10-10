# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
        left=0
        right=len(nums)-1
        tmp=TreeNode(10001,None)
        head= tmp
        def bst(left,right,tmp):
            mid = (left+right)//2
            if nums[mid] == tmp.val:
                return
            tmp2 = TreeNode(nums[mid])
            if tmp2.val < tmp.val:
                tmp.left = tmp2
            else:
                tmp.right = tmp2
            if mid == left:
                bst(mid+1,right,tmp2)
            elif mid == right:
                bst(left,mid-1,tmp2)
            else:
                bst(left,mid-1,tmp2)
                bst(mid+1,right,tmp2)
                
                
        bst(left,right,head)
        return head.left
            
            