class Solution:
    def climbStairs(self, n: int) -> int:
        a = 1
        b = 1

        for i in range(2,n+2):
            c = a + b
            a = b
            b = c
        
        return a