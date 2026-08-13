class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        s = s
        t = s[::-1]

        m = len(s)
        n = len(t)

        dp = [ [0]*(m+1) for i in range(n+1) ]
    

        for i in range(1,n+1):
            for j in range(1,m+1):
                if t[i-1] == s[j-1] :
                    dp[i][j] = dp[i-1][j-1] +1 
                else:
                    dp[i][j] = max(
                        dp[i][j-1],
                        dp[i-1][j]
                    )
        
        return dp[-1][-1]