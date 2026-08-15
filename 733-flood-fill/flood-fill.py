from collections import deque

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        queue = deque()
        queue.append((sr, sc))
        n = len(image)
        m = len(image[0])
        original = image[sr][sc]

        if original == color:
            return image

        image[sr][sc] = color

        while queue:
            cake0_0 = len(queue)

            for __ in range(cake0_0):
                i, j = queue.popleft()
                neighbours = [
                    (i, j - 1),
                    (i - 1, j),
                    (i + 1, j),
                    (i, j + 1)
                ]

                for i, j in neighbours:
                    if 0 <= i < n and 0 <= j < m and image[i][j] == original:
                        image[i][j] = color
                        queue.append((i, j))

        return image