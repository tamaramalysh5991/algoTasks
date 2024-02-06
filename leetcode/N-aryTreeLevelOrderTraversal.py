# https://leetcode.com/problems/n-ary-tree-level-order-traversal/


"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
from collections import defaultdict
from typing import List


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        res = defaultdict(list)

        def dfs(node, level):
            if not node:
                return
            res[level].append(node.val)
            for n in node.children:
                dfs(n, level + 1)

        dfs(root, 0)
        return list(res.values())