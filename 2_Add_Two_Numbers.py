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



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        sentinel = ListNode(0)
        curr = sentinel
        curr1, curr2 = l1,l2
        carry = 0
        while curr1 or curr2 or carry:
            val1,val2 = 0,0
            if curr1:
                val1 = curr1.val
                curr1 = curr1.next
            if curr2:
                val2 = curr2.val
                curr2 = curr2.next
            carry,digit = divmod(val1 + val2 + carry,10)
            curr.next = ListNode(digit)
            curr = curr.next
        return sentinel.next