# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        q = deque()
        i=1
        if not root:
            return 0
        else:
            q.append((root,i))
            while q:
                x,level = q.popleft()
                if not x.left and not x.right:
                    return level
                if x.left:
                    q.append((x.left,level+1))
                if x.right:
                    q.append((x.right,level+1))
                    
                    