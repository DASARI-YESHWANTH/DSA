# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        lst=[]
        def preorder(node):										
	        if node== None:
		        return
	        preorder(node.left)
	        lst.append(node.val)
	        preorder(node.right)
        preorder(root)
        return lst
        