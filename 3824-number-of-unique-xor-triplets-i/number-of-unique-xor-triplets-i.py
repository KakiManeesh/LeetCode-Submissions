class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        n = len(nums)

        if n <= 2 :
            return n
        count = 0 
        while n :
            count +=1
            n = n >> 1

        return 2**( count ) 