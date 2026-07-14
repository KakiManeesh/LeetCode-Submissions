from math import gcd
from typing import List

class Solution:
    def subsequencePairCount(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        M = max(nums)  

        dp = [[0]*(M+1) for _ in range(M+1)]
        dp[0][0] = 1  

        for x in nums:
            new_dp = [row[:] for row in dp]  
            for g1 in range(M+1):
                for g2 in range(M+1):
                    cnt = dp[g1][g2]
                    if cnt == 0:
                        continue
                    ng1 = gcd(g1, x)
                    new_dp[ng1][g2] = (new_dp[ng1][g2] + cnt) % MOD
                    
                    ng2 = gcd(g2, x)
                    new_dp[g1][ng2] = (new_dp[g1][ng2] + cnt) % MOD
            dp = new_dp

        ans = 0
        for g in range(1, M+1):
            ans = (ans + dp[g][g]) % MOD
        return ans