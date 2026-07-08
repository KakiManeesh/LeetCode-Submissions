from typing import List
import bisect

class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        MOD = 10**9 + 7

        n = len(s)

        # prefix sum of all digits
        sum_prefix = [0] * (n + 1)

        # non-zero digit positions and their concatenation prefix
        pos = []
        concat = [0]
        powers = [1]

        for i, ch in enumerate(s):
            digit = int(ch)
            sum_prefix[i + 1] = sum_prefix[i] + digit

            if digit != 0:
                pos.append(i)
                concat.append((concat[-1] * 10 + digit) % MOD)
                powers.append((powers[-1] * 10) % MOD)

        ans = []

        for l, r in queries:
            # sum of digits in range
            sm = sum_prefix[r + 1] - sum_prefix[l]

            # find non-zero digits inside [l,r]
            left = bisect.bisect_left(pos, l)
            right = bisect.bisect_right(pos, r)

            if left == right:
                ans.append(0)
                continue

            # concatenate digits from left to right-1
            length = right - left
            x = (concat[right] - concat[left] * powers[length]) % MOD

            ans.append((x * sm) % MOD)

        return ans