# Binary Tree in Python
class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

    # Traverse preorder
    def traversePreOrder(self):
        print(self.value, end=' ')
        if self.left:
            self.left.traversePreOrder()
        if self.right:
            self.right.traversePreOrder()

    # Traverse inorder
    def traverseInOrder(self):
        if self.left:
            self.left.traverseInOrder()
        print(self.value, end=' ')
        if self.right:
            self.right.traverseInOrder()

    # Traverse postorder
    def traversePostOrder(self):
        if self.left:
            self.left.traversePostOrder()
        if self.right:
            self.right.traversePostOrder()
        print(self.value, end=' ')

    def __repr__(self):
        return f'Node({self.value})'

        

class BST:
    def __init__(self, value = None):
        newNode = Node(value)
        self.root = newNode

    # Insert 
    def insert(self, value):
        newNode = Node(value)
        if self.root is None:
            self.root = newNode
            return self
        current = self.root
        while True:
            if newNode.value==current.value: 
                return None
            if newNode.value < current.value:
                if current.left is None:
                    current.left = newNode
                    return self
                current = current.left
            else:
                if current.right is None:
                    current.right = newNode
                    return self
                current = current.right

    # To find if a node exists
    def contains(self, value):
        if self.root is None:
            return False
        current = self.root
        while current:
            if value < current.value:
                current = current.left
            elif value > current.value:
                current = current.right
            else:
                return True
        return False

    # Finds minimum value in a subtree
    def minValueNode(self, currentNode):
        while currentNode.left:
            currentNode = currentNode.left
        return currentNode.value

    # Deleting a node
    def deleteNode(self, root, key):
        # Return if the tree is empty
        if root is None:
            return root

        # Find the node to be deleted
        if key < root.key:
            root.left = self.deleteNode(root.left, key)
        elif(key > root.key):
            root.right = self.deleteNode(root.right, key)
        else:
            # If the node is with only one child or no child
            if root.left is None:
                temp = root.right
                root = None
                return temp

            elif root.right is None:
                temp = root.left
                root = None
                return temp

            # If the node has two children,
            # place the inorder successor in position of the node to be deleted
            temp = self.minValueNode(root.right)

            root.key = temp.key

            # Delete the inorder successor
            root.right = self.deleteNode(root.right, temp.key)
        return root
    
    # To print
    def __repr__(self):
        lefts = "left values: "
        rights = 'right values: '
        
        # Traverse the left subtree and add the node values to the 'lefts' string
        left_node = self.root.left
        while left_node:
            lefts += str(left_node.value) + '->'
            left_node = left_node.left
        
        # Traverse the right subtree and add the node values to the 'rights' string
        right_node = self.root.right
        while right_node:
            rights += str(right_node.value) + '->'
            right_node = right_node.right
        
        # Return a string representation of the root node and its subtrees
        return 'root: ' + str(self.root.value) + ' ' + lefts + ' ' + rights    

    def print_tree(self):
        def print_tree_helper(curr_node, depth=0, is_left=None):
            if curr_node is not None:
                print_tree_helper(curr_node.right, depth=depth+1, is_left=False)
                if is_left is None:
                    prefix = ""
                elif is_left:
                    prefix = "├── "
                else:
                    prefix = "└── "
                print("    "*depth + prefix + f"({curr_node.value})")
                print_tree_helper(curr_node.left, depth=depth+1, is_left=True)
        
        print_tree_helper(self.root)


newTree = BST(45)
newTree.insert(40)
newTree.insert(89)
newTree.insert(32)
# print(newTree)
newTree.print_tree()
# print(newTree.contains(45))
# print(newTree.contains(30))
# print(newTree.minValueNode(newTree.root.right))

# root = Node(1)
# root.left = Node(2)
# root.right = Node(3)
# root.left.left = Node(4)
# print("Pre order Traversal: ", end="")
# root.traversePreOrder()
# print("\nIn order Traversal: ", end="")
# root.traverseInOrder()
# print("\nPost order Traversal: ", end="")
# root.traversePostOrder()
