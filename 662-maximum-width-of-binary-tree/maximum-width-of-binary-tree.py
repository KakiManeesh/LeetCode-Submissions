# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:



        stack = [[root,1]]
        ans = 0
        while stack :
            ans = max(ans , stack[-1][1] - stack[0][1]+1)
            n = len(stack)
            for i in range(n):
                node,pos = stack.pop(0)
                if  node.left :
                    stack.append((node.left,pos*2))
                if  node.right :
                    stack.append((node.right,pos*2 + 1))
        return ans
        
        