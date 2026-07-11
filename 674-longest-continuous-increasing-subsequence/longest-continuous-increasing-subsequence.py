class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        i = 0
        ans = 1
        for j in range(1,len(nums)):
            if nums[j-1] >= nums[j] :
                i = j
            ans = max(ans, j-i+1)
        return ans