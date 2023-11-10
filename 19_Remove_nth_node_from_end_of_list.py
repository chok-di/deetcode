# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]: 
        sentinel = ListNode(0)
        sentinel.next = head
        temp = sentinel
        curr = head
        tail = curr
        for i in range(n):
            tail = tail.next
        while tail:
            temp = curr
            curr = curr.next
            tail = tail.next
        temp.next = curr.next
        return sentinel.next