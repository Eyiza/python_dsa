class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
            return
        curr_node = self.head
        while curr_node.next != self.head:
            curr_node = curr_node.next
        curr_node.next = new_node
        new_node.next = self.head

    def prepend(self, data):
        new_node = Node(data)
        curr_node = self.head
        new_node.next = self.head
        if self.head is None:
            new_node.next = new_node
            self.head = new_node
            return
        while curr_node.next != self.head:
            curr_node = curr_node.next
        curr_node.next = new_node
        self.head = new_node

    def delete_node(self, key):
        if self.head is None:
            return
        if self.head.next == self.head and self.head.data == key:
            self.head = None
            return
        curr_node = self.head
        while curr_node.next != self.head:
            if curr_node.next.data == key:
                break
            curr_node = curr_node.next
        if curr_node.next == self.head:
            return
        curr_node.next = curr_node.next.next
        if curr_node.next == self.head:
            self.head = curr_node.next

    def print_list(self):
        curr_node = self.head
        while curr_node:
            print(curr_node.data)
            curr_node = curr_node.next
            if curr_node == self.head:
                break
    
    def __len__(self):
        curr_node = self.head
        count = 0
        while curr_node:
            count += 1
            curr_node = curr_node.next
            if curr_node == self.head:
                break
        return count
    
    def split_list(self):
        size = len(self)
        if size == 0:
            return None
        if size == 1:
            return self.head
        mid = size // 2
        count = 0
        prev = None
        curr = self.head
        while curr and count < mid:
            count += 1
            prev = curr
            curr = curr.next
        prev.next = self.head
        split_cllist = CircularLinkedList()
        while curr.next != self.head:
            split_cllist.append(curr.data)
            curr = curr.next
        split_cllist.append(curr.data)
        self.print_list()
        print(" ")
        split_cllist.print_list()

cllist = CircularLinkedList()
cllist.append("C")
cllist.append("D")
cllist.append("E")
cllist.append("F")
cllist.append("G")
cllist.append("H")
cllist.print_list()
# print(" ")
# cllist.split_list()

        
