class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0])
        def helper(i,j):
            
            if i<0 or j<0 or i>=n or j >= m :
                return 0
            if grid[i][j] == '0' :
                return 0
            if grid[i][j] == '#' :
                return 0

            grid[i][j] = '#'

            helper(i+1,j)
            helper(i-1,j)
            helper(i,j+1)
            helper(i,j-1)
        count = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1' :
                    count += 1
                    helper(i,j)
        return count