# Data structure to store a Binary Tree node
class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __repr__(self):
        return str(self.data)


# Function to perform preorder traversal of the binary tree
def preorder(root):
    if root is None:
        return

    print(root.data, end=' ')
    preorder(root.left)
    preorder(root.right)


# Utility function to swap left subtree with right subtree
def swap(root):
    if root is None:
        return

    root.left, root.right = root.right, root.left


# Function to invert given binary Tree using preorder traversal
def invertBinaryTree(root):
    # base case: if tree is empty
    if root is None:
        return

    # swap left subtree with right subtree
    swap(root)

    # invert left subtree
    invertBinaryTree(root.left)

    # invert right subtree
    invertBinaryTree(root.right)


if __name__ == '__main__':
    """ Construct below tree
              1
            /   \
           /     \
          2       3
         / \     / \
        4   5   6   7
    """

    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    preorder(root)
    print('\n')
    invertBinaryTree(root)
    preorder(root)

# Output
# 1 3 7 6 2 5 4
