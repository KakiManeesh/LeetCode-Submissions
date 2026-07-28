# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        
        hash = {}
        for i in range(len(inorder)):
            hash[inorder[i]] = i 

        def solve(inorder,postorder):
            if not inorder or not postorder :
                return None
            n = len(inorder)
            node = TreeNode(postorder[-1])
            pos = hash[postorder[-1]]
            left_size = pos - hash[inorder[0]] 
            
            next_left_in   = inorder[         : left_size   ]
            next_left_post  = postorder[ :left_size ]
            next_right_in  = inorder[ left_size + 1 :       ] 
            next_right_post = postorder[ left_size : n-1 ]

            node.left  =  solve(next_left_in,next_left_post)
            node.right =  solve(next_right_in , next_right_post)
            return node
        
        return solve(inorder,postorder)