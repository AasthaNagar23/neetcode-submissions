# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def max_depth(node):
            if node is None:
                return 0
            left=max_depth(node.left)
            if left==-1:
                return -1
            
            right=max_depth(node.right)
            if right==-1:
                return -1
            
            if abs(left-right)>1:
                return -1
                
            return max(left,right)+1
        return max_depth(root)!=-1
        