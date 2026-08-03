# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = None
#         self.right = None

class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0

        # Find height
        h = 0
        curr = root
        while curr:
            h += 1
            curr = curr.left

        if h == 1:
            return 1

        last_level_nodes = 2 ** (h - 1)

        def exists(idx):
            node = root

            left = 0
            right = last_level_nodes - 1

            for _ in range(h - 1):

                mid = (left + right) // 2

                if idx <= mid:
                    node = node.left
                    right = mid
                else:
                    node = node.right
                    left = mid + 1

                if not node:
                    return False

            return True

        low = 0
        high = last_level_nodes - 1

        while low <= high:

            mid = (low + high) // 2

            if exists(mid):
                low = mid + 1
            else:
                high = mid - 1

        nodes_before_last = 2 ** (h - 1) - 1

        return nodes_before_last + low