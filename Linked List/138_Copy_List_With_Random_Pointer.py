"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
import copy
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        map = {None:None}
        curr = head
        while curr:
            copy_node = ListNode(curr.val)
            map[curr] = copy_node
            curr = curr.next
        curr = head
        while curr:
            copy_node = map[curr]
            copy_node.next = map[curr.next]
            copy_node.random = map[curr.random]
            curr = curr.next
        return map[head]