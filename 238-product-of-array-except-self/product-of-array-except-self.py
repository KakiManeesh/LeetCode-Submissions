class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix_products = [1] * n 
        suffix_products = [1] * n  
        
        prefix = 1

        for i in range(n):
            prefix_products[i] = prefix
            prefix *= nums[i]
        

        suffix = 1
        for i in range(n - 1, -1, -1):
            suffix_products[i] = suffix
            suffix *= nums[i]

        result = [prefix_products[i] * suffix_products[i] for i in range(n)]
        
        return result
