class Solution:
    def minPairSum(self, nums: List[int]) -> int:

        nums.sort()
        max_ = 0
        n = len(nums)
        for i in range(0,n//2):
            max_ = max(max_ , nums[i] + nums[n-i-1] )
        return max_