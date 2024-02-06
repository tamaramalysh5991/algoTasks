# Data structure to store a Binary Tree node
class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __repr__(self):
        return str(self.data)


# Function to find number of nodes in the binary tree
def size(root):
    if root is None:
        return 0

    return 1 + size(root.left) + size(root.right)


# Function to check if a given binary tree is a complete binary tree
# and each node has value is greater than the value of its parent.
def isMinHeap(root, i, n):
    # base case
    if root is None:
        return True

    # complete binary tree: out of valid not index range
    if i >= n:
        return False

    # current node has greater value than its left or right child
    if ((root.left and root.left.data <= root.data) or
            (root.right and root.right.data <= root.data)):
        return False

    # check for left and right subtree
    return isMinHeap(root.left, 2 * i + 1, n) and \
           isMinHeap(root.right, 2 * i + 2, n)


# Function to check if a given binary tree is a min heap or not
def isHeap(root):
    i = 0
    return isMinHeap(root, i, size(root))


if __name__ == '__main__':

    """ Construct below binary tree
               2
             /   \
            /     \
           3       4
          / \     / \
         /   \   /   \
        5     6 8    10
    """

    root = Node(2)
    root.left = Node(3)
    root.right = Node(4)
    root.left.left = Node(5)
    root.left.right = Node(6)
    root.right.left = Node(8)
    root.right.right = Node(10)

    if isHeap(root):
        print("Given Binary Tree is a Min-Heap")
    else:
        print("Given Binary Tree is not a Min-Heap")
