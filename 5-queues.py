class Node:
    def __init__(self, value = None, next = None):
        self.value = value
        self.next = next

class Queue:
    def __init__(self, value):
        newNode = Node(value)
        self.first = newNode
        self.last = newNode
        self.length = 1

    def printQueue(self):
        current = self.first
        while current:
           print(current.value)
           current = current.next

    def getFirst(self):
        if self.first is None:
           print("First: null")
        else:
           print("First: " + self.first.value)

    def getLast(self):
        if self.last is None:
           print("Last: null")
        else:
           print("Last: " + self.last.value)

    def getLength(self):
        print("Length: " + self.length)

    def makeEmpty(self):
        self.first = None
        self.last = None
        self.length = 0

    def enqueue(self, value):
        newNode = Node(value)
        if self.length == 0:
           self.first = newNode
           self.last = newNode
        else:
           self.last.next = newNode
           self.last = newNode
        self.length += 1
        return self
    
    def dequeue(self):
        if self.length == 0:
            return None

        current = self.first
        if self.length == 1:
            self.first = None
            self.last = None
        else:
            self.first = self.first.next
            current.next = None
        self.length -= 1
        return current



def test():
    myQueue = Queue(2)
    myQueue.enqueue(1)

    # (2) Items - Returns '2' Node
    if myQueue.length != 0:
        print(myQueue.dequeue().value)
    else:
        print("undefined")

    # (1) Item - Returns '1' Node
    if myQueue.length != 0:
        print(myQueue.dequeue().value)
    else:
        print("undefined")

    # (0) Items - Returns undefined
    if myQueue.length != 0:
        print(myQueue.dequeue().value)
    else:
        print("undefined")


test() 

'''
 EXPECTED OUTPUT:
    ----------------
    2
    1
    undefined
'''
   


