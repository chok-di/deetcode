# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if n == 0:
            return head
        left,right = head, head
        for i in range(0,n):
            right = right.next
        if not right:
            head = head.next
            return head
        while right and right.next:
            left = left.next
            right = right.next
        
        left.next = left.next.next
        return head
        