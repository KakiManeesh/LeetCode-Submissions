class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:

        n = len( grid    )
        m = len( grid[0] )
        empty = 0  
        start_row = start_col = 0
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] != -1:
                    empty += 1
                if grid[i][j] == 1:
                    start_row, start_col = i, j
        ans = 0
        def solve(row , col,visited_count   ):
            nonlocal ans
            if row<0 or col<0 or row>n-1 or col>m-1 :
                return 

            if grid[row][col] == -1 :
                return
            
            if grid[row][col] == 2 :
                if visited_count == empty :
                    ans +=1
                return
            
            grid[row][col] = -1
            solve( row , col + 1 , visited_count + 1 )
            solve( row + 1 , col , visited_count + 1 )
            solve( row - 1 , col , visited_count + 1 )
            solve( row , col - 1 , visited_count + 1 )
            grid[row][col] = 0
        
        solve( start_row , start_col , 1 )
        return ans