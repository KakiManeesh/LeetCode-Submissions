# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        
        count = 0

        slow = head
        fast = head
        while fast and fast.next :
            prev = slow
            slow = slow.next
            fast = fast.next.next
            count +=1
        if fast :
            prev = slow
            slow = slow.next
        prev.next= None
        slowhead = slow
        curr = slow
        prev_node = None
        while curr  :
            next_node = curr.next
            temp = curr
            curr.next = prev_node
            prev_node = curr
            curr = next_node

        rev_head = prev_node

        current1 = head
        current2 = rev_head
        for i in range(count):
            temp = current1.next
            temp2 = current2.next
            current1.next = current2
            current2.next = temp
            current1 = temp
            current2 = temp2
        return head