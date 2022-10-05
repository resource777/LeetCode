# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        tmp =[]
        while list1:
            tmp.append(list1.val)
            list1=list1.next
        while list2:
            tmp.append(list2.val)
            list2=list2.next
        tmp.sort(reverse=True)
        print(tmp)
        
        tmp2 = None
        for i in range(len(tmp)):
            ans = ListNode()
            ans.val = tmp[i]
            ans.next = tmp2
            tmp2 = ans
            
        return tmp2
            