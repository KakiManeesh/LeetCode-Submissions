class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        
        n = len(grid)
        m = len(grid[0])

        new = [ [None]*m for i in range(n) ]

        for i in range(n):
            for j in range(m):

                current = ( i*m + j )
                new_pos = ( current + k )%( m*n)

                new_i = (new_pos)//(m)
                new_j = (new_pos) % m
                new[new_i][new_j] = grid[i][j]
        return new