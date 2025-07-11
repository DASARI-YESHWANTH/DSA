# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def solve(node):
            if node== None:
                return 0
            lefthei=solve(node.left)
            righthei=solve(node.right)
            return 1+max(lefthei,righthei)
        l=solve(root) 
        return l       