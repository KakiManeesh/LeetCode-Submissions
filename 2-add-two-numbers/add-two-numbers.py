# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        a = l1
        b = l2
        new = ListNode(0)
        curr = new
        carry = 0
        while a and b :
            sum = a.val + b.val  + carry
            curr.next = ListNode(sum%10)
            carry = sum//10
            a = a.next
            b = b.next
            curr = curr.next
        if b :
            while b :
                sum = b.val + carry
                curr.next = ListNode(sum%10)
                carry = sum // 10
                b = b.next
                curr = curr.next
        else:            
            while a :
                sum = a.val + carry
                curr.next = ListNode(sum%10)
                carry = sum // 10
                a = a.next
                curr = curr.next
        if carry :
            curr.next = ListNode(1)
        return new.next