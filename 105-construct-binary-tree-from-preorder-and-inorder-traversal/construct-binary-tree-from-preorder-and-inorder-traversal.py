# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        def solve(  inorder , preorder ):
            if not inorder or not preorder :
                return 
            node = TreeNode(preorder[0])
            pos = inorder.index(preorder[0])
            next_left_in  = inorder[ : pos ]
            next_right_in = inorder[ pos+1 : ]

            count_of_left = pos-1 

            next_left_pre = preorder[1: pos +1 ]
            next_right_pre = preorder[  pos+1 : ]

            
            node.left = solve(next_left_in , next_left_pre)
            node.right = solve( next_right_in , next_right_pre)
            return node

        root = solve( inorder , preorder )
        return root
