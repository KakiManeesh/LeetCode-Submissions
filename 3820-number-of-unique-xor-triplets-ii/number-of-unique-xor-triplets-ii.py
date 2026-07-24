class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        
        visited= set()

        for i in nums :
            for j in nums :
                visited.add(i^j)
        ans = set()
        for k in visited :
            for j in nums :
                ans.add(j^k)
        
        return len(ans)