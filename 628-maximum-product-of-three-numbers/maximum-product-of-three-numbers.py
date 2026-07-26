class Solution:
    def maximumProduct(self, nums: List[int]) -> int:

        if len(nums) == 3 :
            return nums[0]*nums[1]*nums[2]

        nums.sort()
        
        max1 = nums[-1] * nums[-2] * nums[-3]
        
        max2 = nums[0] * nums[1] * nums[2]

        max3 =  nums[0] * nums[1] * nums[-1]
        
        return max(max1,max3)
