from collections import deque


# Data structure to store a Binary Tree node
class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


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


# Iterative Function to invert given binary Tree using queue
def invertBinaryTree(root):
    # base case: if tree is empty
    if root is None:
        return

    # maintain a queue and push push root node
    q = deque()
    q.append(root)

    # run till queue is empty
    while q:

        # pop top node from queue
        curr = q.popleft()

        # swap left child with right child
        swap(curr)

        # push left child of popped node to the queue
        if curr.left:
            q.append(curr.left)

        # push right child of popped node to the queue
        if curr.right:
            q.append(curr.right)


if __name__ == '__main__':
    ''' Construct below tree
              1
            /   \
           /     \
          2       3
         / \     / \
        4   5   6   7
    '''

    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)

    invertBinaryTree(root)
    preorder(root)
