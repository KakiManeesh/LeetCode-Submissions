class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        a = [False]*(len(nums))
        out = []
        for i in nums :
            if  a[i-1] :
                out.append(i)
            else:
                a[i-1] = True
        return out