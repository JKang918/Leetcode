from typing import List
import heapq
def connectSticks(sticks: List[int]) -> int:

    ans = []

    heapq.heapify(sticks)

    while len(sticks) > 1:
        ans.append(heapq.heappop(sticks) + heapq.heappop(sticks))
        
        heapq.heappush(sticks, ans[-1])
        
    return sum(ans)