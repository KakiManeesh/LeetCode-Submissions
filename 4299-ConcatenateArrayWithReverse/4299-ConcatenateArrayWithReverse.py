# Last updated: 7/3/2026, 12:48:26 PM
class Solution:
    def concatWithReverse(self, nums: list[int]) -> list[int]:
        return nums+nums[::-1]