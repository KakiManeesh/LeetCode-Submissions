# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        
        stack1 = []
        stack2 = []
        def push_left(curr,stack1):
            while curr :
                stack1.append(curr)
                curr =  curr.left
        push_left(root,stack1)

        def push_right(curr,stack2):            
            while curr :
                stack2.append(curr)
                curr =  curr.right
        push_right(root,stack2)

        def next(stack):
            last = stack.pop()
            push_left(last.right,stack)
            return last
        
        def prev(stack):
            last = stack.pop()
            push_right( last.left , stack )
            return last
        
        def peek_left():
            return stack1[-1]
        
        def peek_right():
            return stack2[-1]

        
        while stack1 and stack2 :
            first_node = peek_left()
            last_node = peek_right()

            if first_node == last_node :
                return False

            first = first_node.val
            last =  last_node.val

            if (first + last) == k :
                return True
            elif first+last > k :
                prev(stack2)
            else:
                next(stack1)
        return False