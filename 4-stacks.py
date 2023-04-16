class Node:
    def __init__(self, value = None, next = None):
        self.value = value
        self.next = next

class Stack():
    def __init__(self, value):
        newNode = Node(value)
        self.top = newNode
        self.length = 1

    def printStack(self):
        current = self.top
        while current:
           print(current.value)
           current = current.next
    
    def getTop(self):
        if self.top is None:
           print("Top: null")
        else:
           print("Top: " + self.top.value)

    def getLength(self):
        print("Length: " + self.length)
           
    def makeEmpty(self):
        self.top = None
        self.length = 0

    def push(self, value):
       newNode = Node(value)
       if self.length == 0:
           self.top = newNode
       else:
           newNode.next = self.top
           self.top = newNode
       self.length += 1
       return self
    
    def pop(self):
        if self.length == 0:
            return None
        current = self.top
        self.top = self.top.next
        current.next = None
        self.length -= 1
        return current


def test():
    myStack = Stack(2)
    myStack.push(1)
    myStack.printStack()

    # (2) Items - Returns '1' Node
    if myStack.length != 0:
        print(myStack.pop().value)
    else:
        print("undefined")

    # (1) Item - Returns '2' Node
    if myStack.length != 0:
        print(myStack.pop().value)
    else:
        print("undefined")

    # (0) Items - Returns undefined
    if myStack.length != 0:
        print(myStack.pop().value)
    else:
        print("undefined")


test() 

'''
 EXPECTED OUTPUT:
    ----------------
    1
    2
    undefined
'''
   

