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
        ans = []
        nodes = []
        def solve(node):

            if not node :
                return
            
            solve(node.left)
            nodes.append(node)
            ans.append(node.val)
            solve(node.right)
        solve(root)
        print(ans)

        n  = len(ans)
        for i in range(n-1,0,-1) :
            if ans[i-1] > ans[i] :
                break
        
        for j in range(n-1):
            if ans[j] > ans[j+1] :
                break
        nodes[i].val,nodes[j].val  = nodes[j].val,nodes[i].val