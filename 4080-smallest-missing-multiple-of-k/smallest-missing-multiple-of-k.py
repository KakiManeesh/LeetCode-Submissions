class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        p = k
        while True :
            if k not in  nums :
                return k
            k += p