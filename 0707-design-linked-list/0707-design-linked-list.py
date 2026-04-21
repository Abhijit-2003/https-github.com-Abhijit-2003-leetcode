class MyLinkedList:

    class Node:
        def __init__(self, val):
            self.val = val
            self.next = None

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.length:
            return -1

        temp = self.head
        for _ in range(index):
            temp = temp.next

        return temp.val

    def addAtHead(self, val: int) -> None:
        node = self.Node(val)

        if self.length == 0:
            self.head = self.tail = node
        else:
            node.next = self.head
            self.head = node

        self.length += 1

    def addAtTail(self, val: int) -> None:
        node = self.Node(val)

        if self.length == 0:
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node

        self.length += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0:
            self.addAtHead(val)
            return

        if index > self.length:
            return

        if index == 0:
            self.addAtHead(val)
            return

        if index == self.length:
            self.addAtTail(val)
            return

        temp = self.head
        for _ in range(index - 1):
            temp = temp.next

        node = self.Node(val)
        node.next = temp.next
        temp.next = node

        self.length += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.length:
            return

        if index == 0:
            self.head = self.head.next
            if self.length == 1:
                self.tail = None
            self.length -= 1
            return

        temp = self.head
        for _ in range(index - 1):
            temp = temp.next

        if temp.next == self.tail:
            self.tail = temp

        temp.next = temp.next.next
        self.length -= 1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)