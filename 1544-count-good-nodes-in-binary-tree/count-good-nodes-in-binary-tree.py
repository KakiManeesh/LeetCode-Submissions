# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        count = 0

        def solve(node,stack):
            nonlocal count

            if not node :
                return 
            didweadd = False
            if stack[-1] <= node.val :
                count +=1
                stack.append(node.val)
                didweadd = True 
            
            solve(node.left,stack)
            solve(node.right,stack)

            if didweadd :
                stack.pop()
            return 
        solve(root,[root.val])

        return count