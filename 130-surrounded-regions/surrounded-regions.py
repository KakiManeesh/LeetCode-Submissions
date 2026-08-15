from collections import deque
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        stack = deque()
        n = len(board)
        m = len(board[0])

        for i in range(m):
            if board[0][i] == 'O' :
                stack.append((0,i))
            if board[n-1][i] == 'O' :
                stack.append((n-1,i))
        
        for i in range(n):
            if board[i][0] == 'O':
                stack.append((i,0))
            if board[i][m-1] == 'O':
                stack.append((i,m-1))
        while stack :
            temp = len(stack)
            for _ in range(temp):
                i,j = stack.popleft()
                board[i][j] = '-'
                neighbour = [(i+1,j),(i,j+1),(i-1,j),(i,j-1)]

                for i,j in neighbour :
                    if i >=0 and j >= 0 and i < n and j < m  and board[i][j]=='O':
                        stack.append((i,j))
        for i in range(n):
            for j in range(m) :
                if board[i][j] == 'X':
                    continue
                if board[i][j] == "O" :
                    board[i][j] = 'X'
                else:
                    board[i][j] = 'O'