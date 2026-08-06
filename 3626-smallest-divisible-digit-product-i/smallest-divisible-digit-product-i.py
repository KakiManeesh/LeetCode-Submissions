class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        def helper(n):
            prod = 1
            while n and prod != 0 :
                prod = prod * (n%10)
                n = n//10
            return prod

        while True :
            if helper(n)%t == 0 :
                return n
            n += 1
        return n