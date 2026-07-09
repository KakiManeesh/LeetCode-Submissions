import sys
sys.set_int_max_str_digits(10**4)
class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        sum_ = 0
        for i in num :
            sum_ = sum_*10 + i
        num = sum_
        num = num + k
        num = str(num)
        num = list(num)
        for i in range(len(num)) :
            num[i] = int(num[i])
        return num