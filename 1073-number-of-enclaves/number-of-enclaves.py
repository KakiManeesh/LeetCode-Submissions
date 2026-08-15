class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        queue = deque()

        for i in range(n):
            if grid[i][0] == 1:
                queue.append((i, 0))
                grid[i][0] = 0

            if grid[i][m - 1] == 1:
                queue.append((i, m - 1))
                grid[i][m - 1] = 0

        for j in range(m):
            if grid[0][j] == 1:
                queue.append((0, j))
                grid[0][j] = 0

            if grid[n - 1][j] == 1:
                queue.append((n - 1, j))
                grid[n - 1][j] = 0

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while queue:
            i, j = queue.popleft()

            for di, dj in directions:
                ni, nj = i + di, j + dj

                if 0 <= ni < n and 0 <= nj < m and grid[ni][nj] == 1:
                    grid[ni][nj] = 0
                    queue.append((ni, nj))
        count = 0

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    count += 1

        return count
