class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self,value):
        newNode = Node(value)
        self.head = newNode
        self.tail = newNode
        self.length = 1

    def push(self,data):
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
        if self.length == 0:
            self.head = None
            self.tail = None
        return current
    
    def shift(self):
        if self.head is None:
            return None
        temp = self.head
        self.head = self.head.next
        self.length -= 1
        if self.length == 0:
            self.tail = None
        temp.next = None
        return temp
    
    def unshift(self,data):
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
        temp = self.head
        for i in range(index):
            temp = temp.next
        return temp
    
    def set(self,index,data):
        temp = self.get(index)
        if temp:
            temp.data = data
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
        temp = self.get(index-1)
        newNode.next = temp.next
        temp.next = newNode
        self.length += 1
        return True
    
    def remove(self,index):
        if index < 0 or index >= self.length:
            return False
        if index == self.length-1:
            return self.pop()
        if index == 0:
            return self.shift()
        temp = self.get(index-1)
        temp.next = temp.next.next
        self.length -= 1
        return True
    
    def reverse(self):
        if self.head is None:
            return None
        temp = self.head
        self.head = self.tail
        self.tail = temp
        pre = None
        next = None
        for i in range(self.length):
            next = temp.next
            temp.next = pre
            pre = temp
            temp = next
        return self
    
    def __repr__(self):
        if self.head is None:
            print("Linked list is empty")
            return
        temp = self.head
        llstr = ''
        while temp:
            llstr += str(temp.data) + " ---> "
            temp = temp.next
        return llstr            
        

# newlist = LinkedList()
# e1 = Node(1)
# e2 = Node(2)
# e3 = Node(3)
# newlist.head = e1
# newlist.tail = e3
# e1.next = e2
# print(newlist.tail.data)


newlist1 = LinkedList("Mon")
newlist1.push("Tues")
newlist1.push("Wed")
newlist1.push("Thur")
newlist1.push("Fri")
newlist1.pop()
print(newlist1)
