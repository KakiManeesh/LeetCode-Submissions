class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n, m = len(s), len(t)

        dp = [[0] * (m + 1) for _ in range(n + 1)]

        # empty t can be formed in 1 way
        for i in range(n + 1):
            dp[i][0] = 1

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if s[i-1] == t[j-1]:
                    # take + not take
                    dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
                else:
                    # Not take 
                    dp[i][j] = dp[i-1][j]
        return dp[n][m]