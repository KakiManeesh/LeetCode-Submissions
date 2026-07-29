from collections import Counter
from math import comb

class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        LIMIT = k + 1

        cnt = Counter()
        n = len(s)

        for c, f in Counter(s).items():
            cnt[c] = f // 2

        mid = ""
        for c, f in Counter(s).items():
            if f & 1:
                mid = c
                break

        def ways(cnt):
            rem = sum(cnt.values())
            ans = 1
            left = rem

            for c in "abcdefghijklmnopqrstuvwxyz":
                f = cnt[c]
                if f:
                    ans *= comb(left, f)
                    if ans > LIMIT:
                        return LIMIT
                    left -= f
            return ans

        if ways(cnt) < k:
            return ""

        ans = []

        while sum(cnt.values()):

            for ch in "abcdefghijklmnopqrstuvwxyz":

                if cnt[ch] == 0:
                    continue

                cnt[ch] -= 1

                w = ways(cnt)

                if w >= k:
                    ans.append(ch)
                    break

                k -= w
                cnt[ch] += 1

        first = "".join(ans)
        return first + mid + first[::-1]