# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        left,right = head,head.next
        ans = right
        temp = right.next
        while left and right:
            right.next = left
            right = temp.next if temp else None
            left.next = right if right else temp
            left = temp
            temp = right.next if right else None
        return ans