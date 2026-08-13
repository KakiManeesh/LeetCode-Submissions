class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])        
        prev = [float('inf')]*(n+1)
        prev[1] = 0
        for i in range( m ) :
            for j in range(1,n+1):
                prev[j]=min( prev[j] , prev[j-1] ) + grid[i][j-1]
            
        return prev[-1]