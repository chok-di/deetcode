# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        sentinel = ListNode(0)
        curr = sentinel
        while True:
            next_i = None
            for i in range(len(lists)):
                if not lists[i]:
                    continue
                if (next_i is None) or (lists[i].val < lists[next_i].val):
                    next_i = i
            if next_i is None:
                break
            curr.next = lists[next_i]
            lists[next_i] = lists[next_i].next
            curr = curr.next
        
        return sentinel.next
        

            