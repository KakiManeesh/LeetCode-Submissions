import math
class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        sumEven = (n)*(n+1)
        sumOdd = sumEven - n

        return math.gcd(sumEven , sumOdd)