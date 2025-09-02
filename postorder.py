class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def postorder_traversal(node):
    if node:
        postorder_traversal(node.left)
        postorder_traversal(node.right)
        print(node.data, end=" ")

root=Node(4)
root.left=Node(2)
root.right=Node(6)
root.left.left=Node(1)
root.left.right=Node(3)
root.right.left=Node(5)
root.right.right=Node(7)

print("Postorder Traversal: ", end=" ")
postorder_traversal(root)