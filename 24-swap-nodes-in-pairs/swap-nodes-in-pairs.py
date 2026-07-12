# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        prev = None
        while  current and current.next :
            if prev :
                prev.next = current.next
            else:
                head = current.next

            temp = current.next
            current.next = current.next.next
            temp.next = current
            prev = current
            current = current.next
        return head
