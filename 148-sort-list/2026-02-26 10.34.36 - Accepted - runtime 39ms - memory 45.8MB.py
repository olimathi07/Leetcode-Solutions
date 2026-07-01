# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l=[]
        while head:
            l.append(head.val)
            head=head.next
        d=ListNode(0)
        c=d
        l.sort()
        for i in l:
              c.next=ListNode(i)
              c=c.next
        return d.next