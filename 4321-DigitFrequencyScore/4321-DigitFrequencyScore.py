# Last updated: 7/3/2026, 12:48:27 PM
class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        n = sorted(map(int, str(n)))

        total = 0
        curr_num = n[0]
        freq = 1

        for i in range(1, len(n)):
            if n[i] == n[i - 1]:
                freq += 1
            else:
                total += curr_num * freq
                curr_num = n[i]
                freq = 1

        total += curr_num * freq

        return total