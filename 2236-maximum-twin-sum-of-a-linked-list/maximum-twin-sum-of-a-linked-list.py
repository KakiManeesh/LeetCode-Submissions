# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional

class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        
        slow, fast = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        prev = None
        while slow:
            slow.next, prev, slow = prev, slow, slow.next  
        
        
        max_sum = 0
        while prev:  
            max_sum = max(max_sum, head.val + prev.val)
            head, prev = head.next, prev.next  
        
        return max_sum
