# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):

        ans = []

        def solve(node):
            if not node :
                return None
            solve(node.left)
            ans.append(node.val)
            solve(node.right)
        solve(root)
        self.ans = ans
        self.pointer = 0
        self.n = len(ans)

    def next(self) -> int:
        self.pointer += 1
        return self.ans[self.pointer-1]
        

    def hasNext(self) -> bool:
        return self.pointer < self.n


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()