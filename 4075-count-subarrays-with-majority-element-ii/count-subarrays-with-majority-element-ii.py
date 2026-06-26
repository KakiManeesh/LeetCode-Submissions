class BIT:
    def __init__(self, n):
        self.bit = [0] * (n + 2)

    def update(self, i, val):
        while i < len(self.bit):
            self.bit[i] += val
            i += i & -i

    def query(self, i):
        s = 0
        while i > 0:
            s += self.bit[i]
            i -= i & -i
        return s


class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        shift = n + 2
        bit = BIT(2 * n + 5)

        pref = 0
        ans = 0

        bit.update(shift, 1)   # prefix sum = 0

        for x in nums:
            if x == target:
                pref += 1
            else:
                pref -= 1

            idx = pref + shift
            ans += bit.query(idx - 1)
            bit.update(idx, 1)

        return ans