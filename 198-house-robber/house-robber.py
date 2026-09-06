class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0]*(n+2)
        a = 0
        b = 0

        for i in range(2,n+2):
            c = max(
                b ,
                a + nums[i-2]
            )
            a = b
            b = c 
        return b