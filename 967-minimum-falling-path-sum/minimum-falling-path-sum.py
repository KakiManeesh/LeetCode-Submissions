class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        dp = [[float('inf')]*(n+1) for i in range(n+1)]

        for i in range(1,n+1):
            dp[1][i] = matrix[0][i-1]


        for i in range(2,n+1):
            for j in range(1,n+1):
                left = float('inf')
                right = float('inf')
                top = float('inf')

                if j != n  :
                    right = dp[i-1][j+1]
            
                if j-1 != 0  :
                    left = dp[i-1][j-1]

                top = dp[i-1][j]

                dp[i][j] = min(left , right , top) + matrix[i-1][j-1]
        for i in dp :
            print(i)
        return min(dp[-1])