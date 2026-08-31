class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        final = set(range(1,len(nums)+1))
        for i in nums :
            final.discard(i)
        return list(final)