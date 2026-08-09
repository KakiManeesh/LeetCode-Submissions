# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        count = 0
        found = False
        ans = None
        def solve(node):
            nonlocal count , found , ans
            if not node :
                return 
            
            if count == k :
                found = True
                ans = node.val
                return 
            if found  :
                return 
            
            solve(node.left)
            count += 1

            if count == k :
                found = True
                ans = node.val
                return 
            solve(node.right)
        solve(root)
        return ans