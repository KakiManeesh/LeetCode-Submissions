class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        i = 0

        n = len(nums)
        left = 1 
        out = 0
        for j in range(0,n) :
            if nums[j] == 1 :
                pass
            elif left :
                left -= 1
            else :
                while not left  :
                    if nums[i] == 0 :
                        left += 1
                    i+=1
                left -=1
            out = max(out,j-i)
        return out
            