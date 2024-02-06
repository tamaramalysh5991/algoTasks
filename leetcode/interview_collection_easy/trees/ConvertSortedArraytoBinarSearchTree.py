import collections
from typing import Optional, List

from leetcode.interview_collection_easy.trees.tree_representation import TreeNode, deserialize


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    class Solution:
        def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
            pass



if __name__ == "__main__":
    # res = deserialize("[3,9,20,null,null,15,7]")
    # res = deserialize("[1,2]")
    res = deserialize("[1,2,3,4,null,null,5]")
    print(res)
    print(Solution().levelOrder(res))