class Solution:
    def processStr(self, s: str, k: int) -> str:
        n = len(s)

        lengths = [0] * (n + 1)

        for i, ch in enumerate(s):
            cur = lengths[i]

            if ch == '*':
                lengths[i + 1] = max(0, cur - 1)
            elif ch == '#':
                lengths[i + 1] = cur * 2
            elif ch == '%':
                lengths[i + 1] = cur
            else:
                lengths[i + 1] = cur + 1

        if k >= lengths[n]:
            return '.'

        for i in range(n - 1, -1, -1):
            ch = s[i]
            cur = lengths[i]

            if ch == '*':
                pass

            elif ch == '#':
                if k >= cur:
                    k -= cur

            elif ch == '%':
                k = cur - 1 - k

            else:
                if k == cur:
                    return ch

        return '.'