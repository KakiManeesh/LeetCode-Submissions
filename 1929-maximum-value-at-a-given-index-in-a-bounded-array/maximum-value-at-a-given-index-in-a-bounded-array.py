class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        def calc(x, cnt):
            if x >= cnt:
                first = x - cnt + 1
                return (first + x) * cnt // 2
            else:
                return x * (x + 1) // 2 + (cnt - x)
        

        low = 1
        high = maxSum

        while low < high :
            mid = (low + high +1 )//2

            left = calc(mid - 1, index)
            right = calc(mid - 1, n - index - 1)

            total = left + mid + right

            if total <= maxSum :
                low = mid
            else:
                high = mid - 1
        return low
