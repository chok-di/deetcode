# initialize a linked list...
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
      if not head or not head.next:
        return head

      first_node = head
      second_node = head.next

      first_node.next = self.swapPairs(second_node.next)
      second_node.next = first_node

      return second_node