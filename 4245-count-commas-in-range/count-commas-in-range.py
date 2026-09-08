class Solution:
    def countCommas(self, n: int) -> int:

        if n<1000 :
            return 0
        
        n = n-999

        if n==10**5 :
            n += 1
        return n