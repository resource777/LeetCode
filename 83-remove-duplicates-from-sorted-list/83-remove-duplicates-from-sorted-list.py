# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cap = ListNode()
        arr = [0 for _ in range(201)]
        while head:
            arr[head.val+100]+=1
            head = head.next
        ccap = cap
        for i in range(0,201):
            if arr[i]:
                tmp = ListNode(i-100,None)
                ccap.next=tmp
                ccap=ccap.next
            
        return cap.next