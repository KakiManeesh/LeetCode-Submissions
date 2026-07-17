
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        '''
        ans = None
        def solve(node ):
            nonlocal ans
            if not node :
                return 0
            if ans :
                return 0
            


            left = solve(node.left )
            right = solve(node.right )

            score = left + right + (node == p) +  (node == q)
            if score == 2 and ans is None:
                ans = node
                return 0

            return score
        solve(root)
        return ans
        '''

        if not root or root==p or root==q :
            return root
        
        left = self.lowestCommonAncestor(root.left,p,q )
        right = self.lowestCommonAncestor(root.right,p,q )

        if left and right :
            return root
        return left or right