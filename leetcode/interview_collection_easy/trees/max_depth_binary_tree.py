from typing import Optional


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return "TreeNode({})".format(self.val)


def deserialize(string):
    if string == "{}":
        return None
    nodes = [
        None if val == "null" else TreeNode(int(val))
        for val in string.strip("[]{}").split(",")
    ]
    kids = nodes[::-1]
    root = kids.pop()
    for node in nodes:
        if node:
            if kids:
                node.left = kids.pop()
            if kids:
                node.right = kids.pop()
    return root



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return 0 if root is None else 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
        # def dfs(node, depth):
        #     if not node:
        #         return depth
        #     return max(dfs(node.left, depth+1), dfs(node.right, depth+1))
        #
        # return dfs(root, depth=0)


if __name__ == "__main__":
    # print(deserialize("[1,2,3,null,null,4,null,null,5]"))
    # print(deserialize("[2,1,3,0,7,9,1,2,null,1,0,null,null,8,8,null,null,null,null,7]"))
    res = deserialize("[3,9,20,null,null,15,7]")
    print(res)
    s = Solution().maxDepth(res)
    print(s)