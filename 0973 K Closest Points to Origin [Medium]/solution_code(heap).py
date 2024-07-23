from typing import List
import heapq

def kClosest(points: List[List[int]], k: int) -> List[List[int]]:

    n = len(points)
    distance = {i : points[i][0] ** 2 + points[i][1] ** 2 for i in range(n)}

    heap = []
    for pointIndex, dist in distance.items():
        heap.append((dist, pointIndex))
    heapq.heapify(heap)

    ans = []
    for _ in range(k):
        dist, pointIndex = heapq.heappop(heap)
        ans.append(points[pointIndex])
    
    return ans