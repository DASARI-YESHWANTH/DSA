# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def solve(node,index):
            if node is None:
                return 0
            lefthei=solve(node.left,index+1)
            righthei=solve(node.right,index+1)
            return 1+max(lefthei,righthei)
        l=solve(root,0)
        return l
        