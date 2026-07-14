class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid[0])

        dp = [float('inf')] * m
        dp[0] = 0

        for row in grid:
            dp[0] += row[0]

            for j in range(1, m):
                dp[j] = min(dp[j], dp[j - 1]) + row[j]

        return dp[-1]