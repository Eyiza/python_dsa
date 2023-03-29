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
        self.tail = newNode
        newNode.prev = current
        self.length += 1
        # print(newNode.prev.value)
        return self

    def pop(self):
        if self.head is None:
            print("Linked list is empty")
            return None
        current = self.tail.prev
        current.next = None
        self.tail = current
        self.length -= 1
    
    def shift(self):
        if self.head is None:
            return None
        # current = self.head
        self.head = self.head.next
        self.head.prev = None
        self.length -= 1
        if self.length == 1:
            self.tail = None
        # current.next = None
        return self

    def unshift(self, value): # Or prepend
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
            return
        newNode.next = self.head
        self.head.prev = newNode
        self.head = newNode
        self.length += 1
        return self
    
    def get(self, index):
        if index < 0 or index >= self.length:
            print("Invalid Index")
            return None
        current = self.head
        for i in range(index):
            current = current.next
        # print(current.value)
        return current
    
    def set(self, index, value):
        current = self.get(index)
        if current:
            current.value = value
            return True
        return False


    def insert(self, index, value):
        if index < 0 or index >= self.length:
            print("Invalid Index") 
            return None
        if index == 0:
            return self.unshift(value)
        if index == self.length:
            return self.push(value)

        newNode = Node(value)
        current = self.get(index-1)
        newNode.next = current.next
        newNode.prev = current
        current.next.prev = newNode
        current.next = newNode
        self.length += 1
        return self
    
    def remove(self, index):
        if index < 0 or index >= self.length:
            print("Invalid Index") 
            return None
        if index == 0:
            return self.shift()
        if index == self.length-1:
            return self.pop()
        current = self.get(index-1)
        current.next = current.next.next
        current.next.prev = current
        print(current.value)
        print(current.next.value)
        print(current.next.prev.value)
        self.length -= 1
        return self

    def delete_node(self, key):
        if self.head is None:
            print("Linked list is empty")
            return None
        if self.head.value == key:
            self.shift()
        if self.tail.value == key:
            self.pop()
        
        current = self.head
        while current.next:
            if current.next.value == key:
                current.next = current.next.next
                current.next.prev = current
                self.length -= 1
            else:
                current = current.next
        return self

    def reverse(self):
        if self.head is None:
            return None
        current = self.head
        while current:
            current.next, current.prev = current.prev, current.next
            current = current.prev
        self.head, self.tail = self.tail, self.head
        return self

    def __str__(self):
        if self.head is None:
            print("Linked list is empty")
            return
        current = self.head
        output = ""
        while current:
            output += str(current.value) + " <-> "
            current = current.next
        return output


newlist1 = DoublyLinkedList("Mon")
newlist1.push("Tues")
newlist1.push("Wed")
newlist1.push("Thur")
newlist1.push("Fri")
print(str(newlist1))
# newlist1.pop()
# newlist1.shift()
# newlist1.unshift("Sun")
# newlist1.get(2)
# newlist1.set(2, "Wednesday")
# newlist1.insert(1, "Fri")
# newlist1.remove(2)
# newlist1.delete_node("Wed")
# newlist1.reverse()
# print(str(newlist1))
# print(newlist1.head.value)
# print(newlist1.head.prev)
# print(newlist1.tail.value)
# print(newlist1.tail.next)
# print(newlist1.length)






