from logging import root


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def inorder_traversal(node):
    if node:
        inorder_traversal(node.left)
        print(node.data, end=" ")
        inorder_traversal(node.right)


root=Node(4)
root.left=Node(2)
root.right=Node(6)
root.left.left=Node(1)
root.left.right=Node(3)
root.right.left=Node(5)
root.right.right=Node(7)

print("Inorder Traversal", end=" ")
inorder_traversal(root)