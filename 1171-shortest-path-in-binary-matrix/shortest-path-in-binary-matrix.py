from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        
        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return -1
        
        if n == 1:
            return 1
            
        queue = deque([(0, 0, 1)]) 
        grid[0][0] = 1
        directions = [
            (0, 1), (0, -1), (1, 0), (-1, 0),
            (1, 1), (1, -1), (-1, 1), (-1, -1)
        ]
        
        while queue:
            row, col, length = queue.popleft()
            
            if row == n - 1 and col == n - 1:
                return length
                
            for dr, dc in directions:
                new_r, new_c = row + dr, col + dc
                
                if 0 <= new_r < n and 0 <= new_c < n and grid[new_r][new_c] == 0:
                    if new_r == n - 1 and new_c == n - 1:
                        return length + 1
                        
                    grid[new_r][new_c] = 1 
                    queue.append((new_r, new_c, length + 1))
                    
        return -1
