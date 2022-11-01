# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q=deque()
        level = 1
        ans = []
        if root == None:
            return ans
        q.append((root,level))
        tmp = []    
        cur_lvl = 1
        while q:
            node,lvl = q.popleft()
            if cur_lvl == lvl:
                 tmp.append(node.val)
            else:
                 ans.append(tmp)
                 cur_lvl=lvl  
                 tmp = []
                 tmp.append(node.val)
            if node.left:
                 q.append((node.left,lvl+1))
            if node.right:
                 q.append((node.right,lvl+1))
        if tmp:
            ans.append(tmp)
        return ans
                 
                 
            