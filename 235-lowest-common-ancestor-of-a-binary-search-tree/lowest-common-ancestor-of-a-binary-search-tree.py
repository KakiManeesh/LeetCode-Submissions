# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        if q.val < p.val :
            p,q = q,p
        
        def solve(node):
            if not node :
                return None
            
            if (p.val <= node.val ) and (node.val <= q.val) :
                return node
            else:
                
                if p.val < node.val :
                    return solve(node.left)
                else:
                    return solve(node.right)
        return solve(root)