# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        ans = []
        to_delete = set(to_delete)

        if root and root.val not in to_delete:
            ans.append(root)
        
        def solve(parent , node , isLeft  ):

            if not node :
                return
            if node.val in to_delete :
                left = node.left
                right = node.right
                if parent :
                    if isLeft :
                        parent.left = None
                    else:
                        parent.right = None
                if left and left.val not in to_delete:
                    ans.append(left)

                solve(None, left, True)

                if right and right.val not in to_delete:
                    ans.append(right)

                solve( None , right ,False )

                return
            
            solve( node , node.left , True )
            solve(node , node.right , False )
        solve(None , root , True )
        return ans