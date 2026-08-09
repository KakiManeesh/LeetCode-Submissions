# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        
        def solve(preorder):
            if not preorder :
                return None
            node = TreeNode(preorder[0])
            
            i = 1
            while i < len(preorder) and preorder[i] < preorder[0]:
                i += 1
                            
            node.left = solve(preorder[1:i])
            node.right = solve(preorder[i:])
            return node
        return solve(preorder)