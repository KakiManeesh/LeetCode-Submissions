# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        prev = None
        first,second = None , None
        def solve(node):
            nonlocal prev,first,second
            if not node :
                return

            solve( node.left)
            if prev and prev.val > node.val:
                if first is None:
                    first = prev
                second = node
            prev = node
            solve(node.right)

        solve(root)
    
        first.val,second.val = second.val , first.val
