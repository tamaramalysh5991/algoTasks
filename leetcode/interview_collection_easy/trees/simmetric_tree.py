import collections
from typing import Optional





# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from leetcode.interview_collection_easy.trees.tree_representation import TreeNode, deserialize


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True

        def is_symmetric(left: Optional[TreeNode], right: Optional[TreeNode]):
            if left is None and right is None:
                return True
            if left is None or right is None:
                return False

            if left.val == right.val:
                out_nodes = is_symmetric(left.left, right.right)
                in_nodes = is_symmetric(left.right, right.left)
                return out_nodes and in_nodes
            else:
                return False

        return is_symmetric(root.left, root.right)

    def isSymmetricIter(self, root):
        if not root:
            return True

        q = collections.deque([root.left, root.right])

        while q:
            t1, t2 = q.popleft(), q.popleft()

            if not t1 and not t2:
                continue
            elif (not t1 or not t2) or (t1.val != t2.val):
                return False

            q += [t1.left, t2.right, t1.right, t2.left]

        return True

if __name__ == "__main__":
    res = deserialize("[1,2,2,3,4,4,3]")
    # res = deserialize("[1,2,2,null,3,null,3]")
    print(res)
    s = Solution().isSymmetric(res)
    print(s)
    print(Solution().isSymmetricIter(res))