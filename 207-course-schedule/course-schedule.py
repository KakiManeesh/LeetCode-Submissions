from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        # b -> a
        adj = {i: [] for i in range(numCourses)}

        for a, b in prerequisites:
            adj[b].append(a)

        visited = set()  # completely processed
        path = set()     # current DFS recursion stack

        def dfs(node):

            if node in path:
                return True      # cycle found

            if node in visited:
                return False     # already processed

            path.add(node)

            for nei in adj[node]:
                if dfs(nei):
                    return True

            path.remove(node)
            visited.add(node)

            return False

        for course in range(numCourses):
            if dfs(course):
                return False

        return True