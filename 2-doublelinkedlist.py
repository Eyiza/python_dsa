class Node:
    def __init__(self, value = None, next = None, prev = None):
        self.value = value
        self.next = next
        self.prev = prev

class DoublyLinkedList:
    def __init__(self, value = None):
        newNode = Node(value)
        self.head = newNode
        self.tail = newNode
        if value:
            self.length = 1
        else:
            self.length = 0

    def push(self, value):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = newNode
        newNode.prev = current

    def prepend(self, value):
        newNode = Node(value)
        newNode.next = self.head
        self.head.prev = newNode
        self.head = newNode

    def delete_node(self, key):
        current = self.head
        if current and current.value == key:
            self.head = current.next
            current.next.prev = None
            current.next = None
            return
        while current and current.value != key:
            current = current.next
        if current is None:
            return
        if current.next:
            current.next.prev = current.prev
        if current.prev:
            current.prev.next = current.next
        current.next = None
        current.prev = None

    def insert(self, index, value):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            self.prepend(value)
            return
        if index == self.length:
            self.push(value)
            return
        newNode = Node(value)
        leader = self.traverseToIndex(index-1)
        follower = leader.next
        leader.next = newNode
        newNode.prev = leader
        newNode.next = follower
        follower.prev = newNode
        self.length += 1

    def traverseToIndex(self, index):
        counter = 0
        current = self.head
        while counter != index:
            current = current.next
            counter += 1
        return current

    # def __str__(self):
    #     current = self.head
    #     output = ""
    #     while current:
    #         output += str(current.value) + " "
    #         current = current.next
    #     return output

    def __str__(self):
        values = []
        node = self.head
        while node:
            values.append(str(node.value))
            node = node.next
        return " <-> ".join(values)


newlist1 = DoublyLinkedList("Mon")
newlist1.push("Tues")
newlist1.push("Wed")
newlist1.push("Thur")
newlist1.push("Fri")
print(str(newlist1))
