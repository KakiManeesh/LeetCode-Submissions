class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        final = set(range(1,len(nums)+1))
        for i in set(nums) :
            final.remove(i)
        return list(final)