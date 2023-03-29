class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self, value = None):
        newNode = Node(value)
        self.head = newNode
        self.tail = newNode
        if value:
            self.length = 1
        else:
            self.length = 0

    def push(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode 
            self.tail = newNode
        self.length += 1
        return self
    
    def pop(self):
        if self.head is None:
            print("Linked list is empty")
            return None
        pre = self.head 
        current = self.head
        while current.next:
            pre=current 
            current=current.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 1:
            self.head = None
            self.tail = None
        return current
    
    def shift(self):
        if self.head is None:
            return None
        current = self.head
        self.head = self.head.next
        self.length -= 1
        if self.length == 1:
            self.tail = None
        current.next = None
        return current
    
    def unshift(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            newNode.next = self.head
            self.head = newNode
        self.length += 1
        return self
    
    def get(self,index):
        if index < 0 or index >= self.length:
            return None
        current = self.head
        for i in range(index):
            current = current.next
        # print(current.data)
        return current
        
    
    def set(self,index,data):
        current = self.get(index)
        if current:
            current.data = data
            return True
        return False
    
    def insert(self,index,data):
        if index < 0 or index > self.length:
            return False
        if index == self.length:
            return self.push(data)
        if index == 0:
            return self.unshift(data)
        newNode = Node(data)
        current = self.get(index-1)
        newNode.next = current.next
        current.next = newNode
        self.length += 1
        return True
    
    def remove(self,index):
        if index < 0 or index >= self.length:
            return False
        if index == self.length-1:
            return self.pop()
        if index == 0:
            return self.shift()
        current = self.get(index-1)
        current.next = current.next.next
        self.length -= 1
        return True
    
    def reverse(self):
        if self.head is None:
            return None
        current = self.head
        self.head = self.tail
        self.tail = current
        pre = None
        # next = None
        for i in range(self.length):
            next = current.next
            current.next = pre
            pre = current
            current = next
        return self
    
    
    def __repr__(self):
        if self.head is None:
            print("Linked list is empty")
            return
        current = self.head
        llstr = ''
        while current:
            llstr += str(current.data) + " ---> "
            current = current.next
        return llstr            
        

newlist1 = LinkedList("Mon")
newlist1.push("Tues")
newlist1.push("Wed")
newlist1.push("Thur")
newlist1.push("Fri")
print(newlist1)
# newlist1.pop()
# newlist1.shift()
# newlist1.unshift("Sun")
# newlist1.get(1)
# newlist1.set(2, "Wednesday")
# newlist1.insert(1, "Fri")
# newlist1.remove(2)
# newlist1.reverse()
# print(newlist1)
