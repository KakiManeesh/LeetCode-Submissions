# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_ = float('-inf')
        def solve(node):
            nonlocal max_
            if not node :
                return 0

            
            left  = max(0,solve(node.left) )
            right = max(0,solve(node.right) )
            
            max_ = max(max_, node.val + left + right)

            return node.val + max(left,right)

        solve(root)
        return max_