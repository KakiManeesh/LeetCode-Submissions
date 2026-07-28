class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        
        def solve(node):
            if not node:
                return
            
            solve(node.left)
            solve(node.right)
            
            if node.left:
                temp_right = node.right
                
                node.right = node.left
                node.left = None
                
                curr = node.right
                while curr.right:
                    curr = curr.right
                
                curr.right = temp_right
                
        solve(root)
