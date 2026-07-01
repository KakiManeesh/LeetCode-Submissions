class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        
        i = 0
        left = k
        n = len(nums)
        out = 0 
        for j in range(n):
            if nums[j] == 1 :
                pass
            elif left :
                left -=1
            else:
                while not left :
                    if nums[i] == 0 :
                        left +=1
                    i+= 1
                left-=1
            out = max(out, j-i+1)
        return out 
            