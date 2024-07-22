from typing import List
import heapq

def topKFrequent(nums: List[int], k: int) -> List[int]:
    
    freq = dict()

    for e in nums:
        if e not in freq:
            freq[e] = 1
        else:
            freq[e] += 1
    
    heap = []
    ans = []
    for key, value in freq.items():
        heap.append((-value, key))

    heapq.heapify(heap)
    
    i = 0
    while i < k:
        x, y = heapq.heappop(heap)
        ans.append(y)
        i += 1

    return ans