# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        left=self.maxDepth(root.left)  #function ko call karne ke liye self ka use kare he 
        right=self.maxDepth(root.right)
        return max(left,right)+1