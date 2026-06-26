from collections import Counter

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        freq = Counter()
        ans = 0

        for x in nums:
            if freq[k - x] > 0:
                ans += 1
                freq[k - x] -= 1
            else:
                freq[x] += 1

        return ans