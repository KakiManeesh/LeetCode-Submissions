class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        n = len(nums1)

        total = [ [nums1[i],nums2[i]] for i in range(n) ]

        total.sort(key = lambda x : -x[1] )

        heap = []

        curr_sum = 0
        ans = 0

        for a,b in total :
            heapq.heappush(heap,a)
            curr_sum += a

            if len(heap) > k :
                curr_sum -= heapq.heappop(heap)

            if len(heap) == k:
                ans = max(ans , curr_sum*b)
        return ans