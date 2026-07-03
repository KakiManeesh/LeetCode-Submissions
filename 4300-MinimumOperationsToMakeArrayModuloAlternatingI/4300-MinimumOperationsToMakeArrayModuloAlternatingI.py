# Last updated: 7/3/2026, 12:48:29 PM
class Solution:
    def minOperations(self, nums: list[int], k: int) -> int:
        cost_even = [0] * k
        cost_odd  = [0] * k

        for i, num in enumerate(nums):
            r = num % k
            for target in range(k):
                d = abs(r - target)
                cost = min(d, k - d)
                if i % 2 == 0:
                    cost_even[target] += cost
                else:
                    cost_odd[target] += cost

        def top2(costs):
            best = second = (float('inf'), -1)
            for r, c in enumerate(costs):
                if c < best[0]:
                    second, best = best, (c, r)
                elif c < second[0]:
                    second = (c, r)
            return best, second

        (ec1, ex1), (ec2, ex2) = top2(cost_even)
        (oc1, oy1), (oc2, oy2) = top2(cost_odd)

        if ex1 != oy1:              
            return ec1 + oc1
        else:                        
            return min(ec2 + oc1,    
                       ec1 + oc2)    