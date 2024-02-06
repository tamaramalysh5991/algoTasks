# Definition for a binary tree node.
from typing import Optional
from leetcode.interview_collection_easy.trees.tree_representation import deserialize


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return



if __name__ == "__main__":
    # print(deserialize("[1,2,3,null,null,4,null,null,5]"))
    # print(deserialize("[2,1,3,0,7,9,1,2,null,1,0,null,null,8,8,null,null,null,null,7]"))
    res = deserialize("[3,9,20,null,null,15,7]")
    print(res)
    s = Solution().maxDepth(res)
    print(s)