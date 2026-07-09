class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        k = 1
        for i in range(len(digits)-1,-1,-1) :
            total = digits[i] + k
            digits[i] = total%10

            k = total // 10

            if k == 0 :
                break
        if k :
            digits.insert(0,1)
        return digits