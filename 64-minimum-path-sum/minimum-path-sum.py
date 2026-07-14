class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])

        prev =  [float('inf')]*(m+1)
        prev[1] = grid[0][0]
        for i in range(1,n+1):
            for j in range(1,m+1):
                curr = prev.copy()
                if i == 1 and j == 1 :
                    continue
                curr[j] = min(prev[j] ,curr[j-1]) + grid[i-1][j-1]
                prev = curr
        return curr[-1]