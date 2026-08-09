# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        curr = None
        next = root
        while next:
            curr = next
            if val < curr.val:
                next = curr.left
            else:
                next = curr.right
                
        if curr.val > val:
            curr.left = TreeNode(val)
        else:
            curr.right = TreeNode(val)
        return root