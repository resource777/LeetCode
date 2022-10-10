# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        tmp = head
        add = set([head])
        cnt=0
        while head:
            print(head.val)
            head = head.next
            if head in add:
                return True
            add.add(head)
        return False