class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def preorder_traversal(node):
    if node:
        print(node.data, end=" ")
        preorder_traversal(node.left)
        preorder_traversal(node.right)

root=Node(4)
root.left=Node(2)
root.right=Node(6)
root.left.left=Node(1)
root.left.right=Node(3)
root.right.left=Node(5)
root.right.right=Node(7)

print("Preorder Traversal: ", end=" ")
preorder_traversal(root)

