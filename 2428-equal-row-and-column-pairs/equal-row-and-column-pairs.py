class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:

        n = len(grid)
        rows = []
        for i in range(n) :
            rows.append(grid[i])
        
        cols = []

        for i in range(n):
            col = []
            for j in range(n):
                col.append( grid[j][i] )
            cols.append(col)
        count = 0
        for row in rows :
            for col in cols :
                if row == col :
                    count += 1
        print("Rows : ")
        for i in rows:
            print(i)
        
        print("Cols :")
        for i in cols :
            print(i)

        return count