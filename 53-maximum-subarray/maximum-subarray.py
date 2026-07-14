class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        '''       
        current = 0
        max_sum = -float('inf')

        for i in nums :
            current += i
            if current > max_sum :
                max_sum = current
            if current < 0 :
                current = 0
        return max_sum
        '''


        dp = [0]*(len(nums))
        dp[0]=nums[0]
        for i in range(1,len(nums)) :
            dp[i] = max( nums[i],dp[i-1]+nums[i] )
        
        return max(dp)