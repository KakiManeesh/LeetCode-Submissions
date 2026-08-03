class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        dp = [0]*(n+3)
    
        dp[0] = 0

        for i in range(n-1,-1,-1):

            value1 = stoneValue[i] - dp[i+1]

            value2 = (stoneValue[i] + stoneValue[i+1] - dp[i+2]) if i+1 < n else float('-inf')

            value3=(stoneValue[i]+stoneValue[i+1]+stoneValue[i+2]-dp[i+3]) if i+2 < n else float('-inf')

            dp[i] = max(value1,value2,value3)


        if dp[0] > 0 :
            return "Alice"
        elif dp[0] < 0 :
            return "Bob"
        else:
            return "Tie"