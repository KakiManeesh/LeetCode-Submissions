class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        
        color = [0]*len(graph)       

        for i in range(len(color)):
            if color[i] == 0 :
                stack = [i]
                color[i] = 1
                while stack :
                    n = len(stack)

                    for ____ in range(n):
                        node = stack.pop(0)

                        for j in graph[node]:
                            if color[j] == color[node]:
                                return False
                            
                            if color[j] == 0 :
                                color[j] = -color[node]
                                stack.append(j)
        return True 