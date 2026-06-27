from collections import Counter

class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        ans = 1

        # Special case for 1
        if 1 in cnt:
            ans = cnt[1] if cnt[1] % 2 else cnt[1] - 1

        for x in cnt:
            if x == 1:
                continue

            cur = x
            pairs = 0

            while cnt.get(cur, 0) >= 2:
                pairs += 1
                cur *= cur

            if cnt.get(cur, 0) == 1:
                ans = max(ans, 2 * pairs + 1)
            else:
                ans = max(ans, max(1, 2 * pairs - 1))

        return ans