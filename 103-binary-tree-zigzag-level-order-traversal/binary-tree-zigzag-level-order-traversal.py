# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        stack = deque([root])
        ans = []
        reverse = 0
        while stack :
            n = len(stack)
            row = deque([])
            for i in range(n):
                node = stack.popleft()
                if reverse :
                    row.appendleft(node.val)
                else:
                    row.append(node.val)
                if node.left :
                    stack.append(node.left)
                if node.right :
                    stack.append(node.right)
            
            ans.append(list(row))

            reverse = (reverse +1)%2
        return ans