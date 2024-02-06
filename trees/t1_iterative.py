from collections import deque


# Data structure to store a Binary Tree node
class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __repr__(self):
        return str(self.data)


# Function to check if a given binary tree is a min heap or not
def isHeap(root):
    # create an empty queue and enqueue root node
    queue = deque()
    queue.append(root)

    # take a boolean flag which becomes true when an empty left or right
    # child is seen for a node
    noneSeen = False

    # run till queue is empty
    while queue:

        # process front node in the queue
        curr = queue.popleft()

        # left child is non-empty
        if curr.left:
            # if either heap-property is violated
            if noneSeen or curr.left.data <= curr.data:
                return False

            # enqueue left child
            queue.append(curr.left)

        # left child is empty
        else:
            noneSeen = True

        # right child is non-empty
        if curr.right:
            # if either heap-property is violated
            if noneSeen or curr.right.data <= curr.data:
                return False

            # enqueue left child
            queue.append(curr.right)

        # right child is empty
        else:
            noneSeen = True

    # we reach here only when the given binary tree is a min-heap
    return True


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
