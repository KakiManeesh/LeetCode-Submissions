class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        nums.sort()

        out = []
        k = 0
        for i in range(nums[0],nums[-1]+1) :
            if i !=  nums[k] :
                out.append(i)
            else:
                k +=1
        return out
        