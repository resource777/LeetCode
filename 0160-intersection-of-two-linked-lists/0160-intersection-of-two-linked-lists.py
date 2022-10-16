# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        a = []
        b = []
        while headA:
            a.append((headA,headA.val))
            headA = headA.next
        while headB:
            b.append((headB,headB.val))
            headB = headB.next
        i = -1
        ans = None
        while True:
            if i>= -min(len(a),len(b)) and a[i][0] == b[i][0]:
                ans = a[i][0]
                i-=1
            else:
                break
        return ans
                