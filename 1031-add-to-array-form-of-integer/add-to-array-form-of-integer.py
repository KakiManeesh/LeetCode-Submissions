class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        for i in range(len(num) - 1, -1, -1):
            total = num[i] + k
            num[i] = total % 10  
            k = total // 10      
            
            if not k:
                break
        
        while k:
            num.insert(0, k % 10)
            k //= 10
            
        return num
