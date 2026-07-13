import heapq
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        heapq.heapify(nums)
        a = []
        while nums :
            a.append(heapq.heappop(nums))
        return a