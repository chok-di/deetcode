class MyLinkedList:

    def __init__(self):
        self.head = ListNode(0)
        self.length = 0
        pass
        

    def get(self, index: int) -> int:
        if index > self.length - 1:
            return -1
        curr = self.head
        for i in range(index + 1):
            curr = curr.next
        return curr.val
        pass
        

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0,val)
        pass
       
        
        

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.length,val)
        pass
        

    def addAtIndex(self, index: int, val: int) -> None:
        if index <= self.length:
            curr = self.head
            for i in range(index):
                curr = curr.next
            to_add = ListNode(val)
            to_add.next = curr.next
            curr.next = to_add
            self.length += 1
    
        pass
            
        

    def deleteAtIndex(self, index: int) -> None:
        if index <= self.length - 1:
            curr = self.head
            for i in range(0,index):
                curr = curr.next
            next_node = curr.next.next if curr.next is not None else None
            curr.next = next_node
            self.length -= 1
        pass
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)