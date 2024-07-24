from typing import List
import heapq

def maxNumberOfApples(self, weight: List[int]) -> int:
    
    heapq.heapify(weight)
    unit = 0
    limit = 5000

    while weight and limit:
        if weight[0] <= limit:
            limit -= heapq.heappop(weight)
            unit += 1
            continue
        else:
            break
    
    return unit