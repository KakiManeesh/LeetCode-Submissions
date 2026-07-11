class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        

        i = 0
        ans = float('inf')
        current = 0
        for j in range(len(nums)):
            current += nums[j]
            while current-nums[i] >= target  :
                current-= nums[i]
                i +=1
            
            if current >= target :
                ans = min(ans , j-i+1  )

        return ans if ans != float('inf') else 0