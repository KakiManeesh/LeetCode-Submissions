class Solution:
    def lengthOfLongestSubsequence(self, nums: List[int], target: int) -> int:
        dp = [  [-1]*(1+target)  for i in range(1+len(nums)) ]
        n = len(nums)

        dp[0][0] = 0


        for i in range(1,n+1):
            for j in range(0,target+1):
                dp[i][j] = dp[i-1][j]
                if j>=nums[i-1] :
                    dp[i][j] = max(
                        dp[i][j],
                        (dp[i-1][j-nums[i-1] ] + 1) if dp[i-1][j-nums[i-1] ] != -1 else float('-inf')
                    )
                    
        return dp[-1][-1]