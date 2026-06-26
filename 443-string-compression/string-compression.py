class Solution:
    def compress(self, chars: List[str]) -> int:

        prev = ""
        count = 0
        out = []

        for ch in chars:
            if ch == prev:
                count += 1
            else:
                if count != 0:
                    out.append(prev)
                    if count > 1:
                        out.extend(list(str(count)))

                prev = ch
                count = 1
        out.append(prev)
        if count > 1:
            out.extend(list(str(count)))

        chars[:] = out
        return len(out)