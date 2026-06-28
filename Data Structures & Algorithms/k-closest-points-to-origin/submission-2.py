class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def euclid(x, y):
            return math.sqrt(x**2 + y**2)

        min_heap = []

        for x, y in points:
            heapq.heappush(min_heap, (-euclid(x, y), [x, y]))
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        return [coord for dist, coord in min_heap]