# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        def dfs(root,target):
            ans = False
            if not root:
                return ans
            if not root.left and not root.right:
                if target == root.val:
                    return True
            if root.left:
                ans = dfs(root.left,target-root.val)
            if root.right: 
                ans = ans | dfs(root.right,target-root.val)
            return ans
            
        return dfs(root,targetSum)
        