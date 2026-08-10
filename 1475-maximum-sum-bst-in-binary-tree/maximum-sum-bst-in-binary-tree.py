# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:

        ans = 0


        def solve( node):
            nonlocal ans
            if not node :
                return (0, True, float("inf"), float("-inf"))

            left = solve(node.left  )
            right = solve(node.right  ) 

            if left[1] and right[1] and  left[3] < node.val < right[2] :
                
                current_sum = left[0] + right[0] + node.val
                ans = max(ans, current_sum)
                
                return (
                    current_sum,
                    True,
                    min(left[2], node.val),
                    max(right[3], node.val)
                )
            
            return (0, False, 0, 0)
        solve(root)
        return ans