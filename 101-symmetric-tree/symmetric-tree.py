# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        def solve(node1,node2):
            if not node1 or not node2 :
                if not node1 and not node2 :
                    return True
                else:
                    return False

            if node1.val != node2.val :
                return False
            
            return (
                solve(node1.left,node2.right)  and 
                solve(node1.right,node2.left)
            )
        return solve( root.left , root.right )