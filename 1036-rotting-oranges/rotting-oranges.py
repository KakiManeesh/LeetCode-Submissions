from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        fresh = set()

        n = len(grid)
        m = len(grid[0])

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    queue.append((i, j))
                elif grid[i][j] == 1:
                    fresh.add((i, j))

        time = 0

        while queue and fresh:
            k = len(queue)

            for _ in range(k):
                i, j = queue.popleft()

                neighbours = [
                    (i, j - 1),
                    (i - 1, j),
                    (i + 1, j),
                    (i, j + 1)
                ]

                for ni, nj in neighbours:
                    if 0 <= ni < n and 0 <= nj < m and grid[ni][nj] == 1:
                        queue.append((ni, nj))
                        grid[ni][nj] = 2
                        fresh.remove((ni, nj))

            time += 1

        return -1 if fresh else time