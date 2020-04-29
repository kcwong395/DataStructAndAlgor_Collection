class Node:
    def __init__(self, value):
        self.val = value
        self.next = None

class MyLinkedList:
    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None
        self.tail = None
        self.size = 0
        

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if index >= self.size:
            return -1
        
        tmp = self.head
        for i in range(index):
            tmp = tmp.next
        
        return tmp.val
        

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        tmp = Node(val)
        tmp.next = self.head
        self.head = tmp
        if self.size == 0:
            self.tail = self.head
        self.size += 1
        

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        if self.size == 0:
            self.head = self.tail = Node(val)
        else:
            tmp = Node(val)
            self.tail.next = tmp
            self.tail = tmp
        self.size += 1
        
        

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if index > self.size:
            return
        
        if index == 0:
            self.addAtHead(val)
        elif index == self.size:
            self.addAtTail(val)
        else:
            cur = self.head
            for i in range(index - 1):
                cur = cur.next
            tmp = cur.next
            cur.next = Node(val)
            cur.next.next = tmp
            self.size += 1
        

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index >= self.size:
            return
        
        if self.size == 1:
            self.head = self.tail = None
        elif index == 0:
            self.head = self.head.next
        else:
            tmp = self.head
            for i in range(index - 1):
                tmp = tmp.next
            if index == self.size - 1:
                self.tail = tmp
            tmp.next = tmp.next.next
            
        self.size -= 1
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)