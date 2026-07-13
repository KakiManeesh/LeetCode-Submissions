class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:

        low  = matrix[0][0]
        high = matrix[-1][-1]
        while low < high :
            mid = low + (high-low)//2
            count = 0
            for i in matrix :
                for  j in i :
                    if j <= mid :
                        count += 1
                    else:
                        break
            
            if count < k :
                low = mid + 1
            else:
                high = mid
        return low