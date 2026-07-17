"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        visited = {}
        def solve( node ):
            nonlocal visited
            if not node :
                return 
            if node in visited :
                return visited[node]
            new_node = Node(node.val)
            visited[node] = new_node
            for neighbor_node in node.neighbors :
                new_node.neighbors.append( solve(neighbor_node) )

            return new_node
        return solve(node)