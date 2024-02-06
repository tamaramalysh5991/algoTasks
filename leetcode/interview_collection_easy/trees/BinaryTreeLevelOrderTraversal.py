import collections
from typing import Optional, List

from leetcode.interview_collection_easy.trees.tree_representation import (
    TreeNode,
    deserialize,
)


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res = [[root.val]]
        nodes = [(1, root)]
        for index, node in nodes:
            if not node.left and not node.right:
                continue
            if len(res) < index + 1:
                res.insert(index, [])
            if node.left:
                res[index].append(node.left.val)
                nodes.append((index + 1, node.left))
            if node.right:
                res[index].append(node.right.val)
                nodes.append((index + 1, node.right))
            # index +=1
        return res


if __name__ == "__main__":
    # res = deserialize("[3,9,20,null,null,15,7]")
    # res = deserialize("[1,2]")
    res = deserialize("[1,2,3,4,null,null,5]")
    print(res)
    print(Solution().levelOrder(res))

from collections import deque


class Solution:
    def levelOrder(self, root):
        if not root:
            return []
        queue, res = deque([root]), []

        while queue:
            cur_level, size = [], len(queue)
            for i in range(size):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                cur_level.append(node.val)
            res.append(cur_level)
        return res


class Solution:
    def levelOrder(self, root):
        if not root:
            return []
        queue, result = deque([root]), []

        while queue:
            level = []
            for i in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(level)
        return result
