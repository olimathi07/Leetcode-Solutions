# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __lt__(self,other):
        return self.val<other.val

ListNode.__lt__ = Node.__lt__

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        head = temp = None
        heap = []
        for i in lists:
            if i:
                heap.append((i.val,i))
        heapq.heapify(heap)
        while(len(heap)>1):
            _,node = heapq.heappop(heap)
            if not head:
                head = node
                temp = head
            else:
                temp.next = node
                temp = node
            if node.next:
                heapq.heappush(heap,(node.next.val,node.next))
        if heap:
            _,node = heapq.heappop(heap)
            temp.next = node
        return head