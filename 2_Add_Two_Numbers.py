# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        h1,h2 = l1,l2
        res = ListNode(0) 
        cur = res
        while (h1 or h2): 
            v1 = h1.val if h1 else 0
            v2 = h2.val if h2 else 0
            sum = v1 + v2 + cur.val
            cur.val = sum % 10
            h1 = h1.next if h1 else None
            h2 = h2.next if h2 else None
            if not (h1 or h2) and sum < 10:
                cur.next = None
                break
            if sum >= 10:
                cur.next = ListNode(1)
            else:
                cur.next = ListNode(0)
            cur = cur.next
        return res
            