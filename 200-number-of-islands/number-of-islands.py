from collections import defaultdict

class Solution:
    def numIslands(self, grid):
        n = len(grid)
        m = len(grid[0])

        graph = defaultdict(list)

        # Build graph
        for i in range(n):
            for j in range(m):

                if grid[i][j] == '0':
                    continue

                node = (i, j)
                graph[node] = []

                directions = [(1,0), (-1,0), (0,1), (0,-1)]

                for dx, dy in directions:
                    ni = i + dx
                    nj = j + dy

                    if (0 <= ni < n and
                        0 <= nj < m and
                        grid[ni][nj] == '1'):

                        graph[node].append((ni, nj))

        visited = set()

        def dfs(node):
            visited.add(node)

            for nei in graph[node]:
                if nei not in visited:
                    dfs(nei)

        islands = 0

        for node in graph:
            if node not in visited:
                islands += 1
                dfs(node)

        return islands