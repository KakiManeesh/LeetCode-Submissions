# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        adj = {}

        def dfs(parent,node):
            if not node :
                return 
            
            if node.val not in adj :
                adj[node.val] = []

            if parent :
                adj[node.val].append(parent.val)
            
            if node.left :
                adj[node.val].append(node.left.val)
            if node.right:
                adj[node.val].append(node.right.val)
            
            dfs( node , node.left )
            dfs( node , node.right )
        
        dfs(None , root)

        max_ = 0
        visited = set()
        def helper( node , height ):
            
            nonlocal max_
            if node in visited :
                return 

            visited.add(node)
            max_ = max( max_ , height )

            for i in adj[node] :
                helper(i , height + 1)
        
        helper(start,0)
        return max_