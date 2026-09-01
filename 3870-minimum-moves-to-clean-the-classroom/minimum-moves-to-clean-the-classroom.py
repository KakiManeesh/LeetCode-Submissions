class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:

        init = None
        n = len(classroom)
        m = len(classroom[0])

        litter = set()
        count = 0

        for i in range(n):
            for j in range(m):
                if classroom[i][j] == "L":
                    litter.add((i, j))
                    count += 1
                elif classroom[i][j] == "S":
                    init = (i, j)

        if count == 0:
            return 0

        q = deque()
        q.append((init[0], init[1], energy, frozenset(), 0))

        visited = {}
        visited[(init[0], init[1], frozenset())] = energy

        while q:

            x, y, e, collected, steps = q.popleft()

            if len(collected) == count:
                return steps

            if e == 0:
                continue

            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:

                xx = x + dx
                yy = y + dy

                if xx < 0 or yy < 0 or xx >= n or yy >= m:
                    continue

                if classroom[xx][yy] == "X":
                    continue

                ee = e - 1
                new_collected = collected

                if classroom[xx][yy] == "R":
                    ee = energy

                if classroom[xx][yy] == "L":
                    new_collected = collected | {(xx, yy)}

                state = (xx, yy, new_collected)

                if state in visited and visited[state] >= ee:
                    continue

                visited[state] = ee
                q.append((xx, yy, ee, new_collected, steps + 1))

        return -1