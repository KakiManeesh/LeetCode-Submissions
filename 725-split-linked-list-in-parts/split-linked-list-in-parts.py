# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        
        count = 0 
        fast = head
        while fast and fast.next :
            fast = fast.next.next 
            count +=2
        if fast :
            count += 1
        
        base = count // k
        extra = count%k

        ans = []
        curr = head

        for i in range(k):
            ans.append(curr)

            part_size = base + (1 if i < extra else 0)

            for _ in range(part_size - 1):
                if curr:
                    curr = curr.next

            if curr:
                nxt = curr.next
                curr.next = None
                curr = nxt
        
        return ans