class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        adj = {}
        for i in range(n):
            adj[i] = []
            for j in range(n):
                if isConnected[i][j] and i!= j :
                    adj[i].append(j)

        visited = set()
        def solve(node):
            if node in visited :
                return
            visited.add(node)
            for i in adj[node] :
                solve(i)
            


        count = 0
        for i in range(n) :
            if i not in visited :
                count += 1
                solve(i)
        return count 