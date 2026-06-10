class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        count = 0
        i = 0

        for j in range(len(s)):
            if j - i + 1 < 3:
                continue

            if j - i + 1 > 3:
                i += 1

            if (
                j - i + 1 == 3
                and s[i] != s[i + 1]
                and s[i] != s[i + 2]
                and s[i + 1] != s[i + 2]
            ):
                count += 1

        return count