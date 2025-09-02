```markdown
# 🌳 Tree

A Python module for building and interacting with Binary Search Trees (BST). This repository includes implementations of common tree traversal algorithms, BST operations, and utility functions for analyzing tree properties.

## 📚 Contents

This repository includes the following modules:

| File Name       | Description |
|----------------|-------------|
| `inorder.py`   | Inorder traversal of a BST (Left → Root → Right) |
| `preorder.py`  | Preorder traversal (Root → Left → Right) |
| `postorder.py` | Postorder traversal (Left → Right → Root) |
| `height.py`    | Calculates the height of a BST |
| `BST_create.py`| Creates a BST from a list of values |
| `BST_insert.py`| Inserts a new node into the BST |
| `BST_search.py`| Searches for a value in the BST |
| `sum_elements.py` | Computes the sum of all node values in the BST |

## 🚀 Getting Started

Clone the repository:

```bash
git clone https://github.com/yourusername/tree.git
cd tree
```

## 🧪 Example Usage

```python
from BST_create import create_bst
from BST_insert import insert
from BST_search import search
from inorder import inorder_traversal
from height import tree_height
from sum_elements import sum_tree

# Create BST from list
values = [10, 5, 15, 3, 7, 12, 18]
root = create_bst(values)

# Insert a new value
insert(root, 6)

# Search for a value
found = search(root, 7)

# Traverse
inorder_traversal(root)

# Tree height
print("Height:", tree_height(root))

# Sum of all elements
print("Sum:", sum_tree(root))
```

## 🧪 Tests

To run tests (if included):

```bash
pytest tests/
```
