# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        arr = []
        added = False
        def solve( node ):
            nonlocal added
            if not node :
                return
            
            solve(node.left)
            if not added and  node.val > val :
                added = True
                arr.append(val)
            arr.append(node.val)
            solve(node.right)
        
        solve(root)
        if not added :
            arr.append(val)

        dummy = TreeNode(-1)       
        curr = dummy

        for i in arr :
            curr.right = TreeNode(i)
            curr = curr.right
        
        return dummy.right