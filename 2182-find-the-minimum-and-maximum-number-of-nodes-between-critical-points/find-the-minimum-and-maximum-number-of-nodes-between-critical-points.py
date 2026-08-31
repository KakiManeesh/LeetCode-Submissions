# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        arr= []

        curr = head
        prev = None
        count = -1
        while curr.next :
            count += 1
            if not prev:
                prev = curr.val
                curr = curr.next
                continue
            if prev < curr.val > curr.next.val :
                arr.append(count)
            elif prev > curr.val < curr.next.val :
                arr.append(count)
            prev = curr.val
            curr = curr.next
        if len(arr) <2 :
            return [-1,-1]
        
        more = float('inf')

        for i in range(1,len(arr)):
            more = min(
                more ,
                arr[i]-arr[i-1]
            )
        print(arr)
        return  [more , arr[-1]-arr[0] ]
