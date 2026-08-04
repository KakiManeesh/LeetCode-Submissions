class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        low = min(nums)
        high = max(nums)

        total = list(range(low,high+1))
        for i in nums :
            total.remove(i)
        return total