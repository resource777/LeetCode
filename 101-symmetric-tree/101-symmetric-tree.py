# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        lc = root.left
        rc = root.right
        def dfs(lc,rc):
            if not lc and rc:
                return False
            if lc and not rc:
                return False
            if not lc and not rc:
                return True
            if lc and rc and lc.val == rc.val:
                return dfs(lc.left,rc.right) and dfs(lc.right,rc.left)
            else:
                return False
        if root:
            return dfs(root.left,root.right)
        