# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_sum=float("-inf")
        def dfs(node):
            nonlocal max_sum
            if node is None:
                return 0
            left=max(0,dfs(node.left))
            right=max(0,dfs(node.right))
            curr_sum=node.val+left+right
            max_sum=max(curr_sum,max_sum)
            return node.val+max(left,right)
        dfs(root)
        return max_sum
        