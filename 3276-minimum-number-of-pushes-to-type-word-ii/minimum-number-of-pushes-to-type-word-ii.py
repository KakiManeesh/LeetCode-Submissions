class Solution:
    def minimumPushes(self, word: str) -> int:
        total = 0
        multiplier = 1
        count = 8

        freq = {}
        for ch in word:
            freq[ch] = freq.get(ch, 0) + 1

        arr = list(freq.values())
        arr.sort(reverse=True)

        for f in arr:
            if count == 0:
                multiplier += 1
                count = 8

            total += f * multiplier
            count -= 1

        return total