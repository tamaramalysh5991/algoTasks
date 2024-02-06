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
    def isValidBSTWrong(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        if getattr(root.left, "val", float('-inf')) < root.val < getattr(root.right, "val", float("inf")):
            return all([self.isValidBST(root.left), self.isValidBST(root.right)])
        else:
            return False

    def isValidBST(self, root, lo=float('-inf'), hi=float('inf')):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True

        if not lo < root.val < hi:
            return False

        return self.isValidBST(root.left, lo, min(root.val, hi)) and self.isValidBST(root.right, max(lo, root.val), hi)

    # def dfs(node, depth):
        #     if not node:
        #         return depth
        #     return max(dfs(node.left, depth+1), dfs(node.right, depth+1))
        #
        # return dfs(root, depth=0)


if __name__ == "__main__":
    # print(deserialize("[1,2,3,null,null,4,null,null,5]"))
    # print(deserialize("[2,1,3,0,7,9,1,2,null,1,0,null,null,8,8,null,null,null,null,7]"))
    # res = deserialize("[2,1,3]")
    # res = deserialize("[5,1,4,null,null,3,6]")
    # res = deserialize("[1,null,1]")
    res = deserialize("[5,4,6,null,null,3,7]")
    print(res)
    s = Solution().isValidBST(res)
    print(s)