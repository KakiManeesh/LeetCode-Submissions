class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        

        max_ = float('-inf')
        n = len(nums)
        for i in range(n-1):
            for j in range(i+1,n):
                current = (nums[i]-1)*(nums[j]-1)
                if max_ < current :
                    max_ = current
        return max_