import heapq

class SmallestInfiniteSet:

    def __init__(self):
        self.heap = list(range(1, 1002))
        heapq.heapify(self.heap)
        self.visited = set()

    def popSmallest(self) -> int:
        a = heapq.heappop(self.heap)
        self.visited.add(a)
        return a

    def addBack(self, num: int) -> None:
        if num in self.visited:
            heapq.heappush(self.heap, num)
            self.visited.remove(num)   